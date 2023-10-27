from copy import deepcopy

from django.db.models.constants import LOOKUP_SEP
from django.db.models.expressions import Expression
from django.db.models.lookups import Transform
from django_filters.filterset import FilterSetMetaclass as _FilterSetMetaclass
from django_filters.rest_framework import FilterSet as _FilterSet
from django_filters.utils import get_model_field

from .filters import AutoFilter, BaseRelatedFilter

__all__ = ('related', 'FilterSetMetaclass', 'SubsetDisabledMixin', 'FilterSet')


def lookups_for_transform(transform):
    def iter_lookups():
        for k, v in transform.output_field.get_lookups().items():
            if issubclass(v, Transform):
                if type(transform) is not v:
                    for subexpr in lookups_for_transform(v(transform)):
                        yield f'{k}{LOOKUP_SEP}{subexpr}'
            else:
                yield k

    return list(iter_lookups())


def lookups_for_field(model_field):
    def iter_lookups():
        for k, v in model_field.get_lookups().items():
            if issubclass(v, Transform):
                for subexpr in lookups_for_transform(v(Expression(model_field))):
                    yield f'{k}{LOOKUP_SEP}{subexpr}'
            else:
                yield k

    return list(iter_lookups())


def related(filterset, filter_name):
    if filterset.relationship:
        return LOOKUP_SEP.join([filterset.relationship, filter_name])
    else:
        return filter_name


class FilterSetMetaclass(_FilterSetMetaclass):
    def __new__(cls, name, bases, attrs):
        attrs['auto_filters'] = cls.get_auto_filters(bases, attrs)
        klass = super().__new__(cls, name, bases, attrs)
        klass.related_filters = {
            k: v
            for k, v in klass.declared_filters.items()
            if isinstance(v, BaseRelatedFilter)
        }

        for v in klass.related_filters.values():
            v.bind_filterset(klass)

        if klass._meta.model is not None:
            for k, v in klass.auto_filters.items():
                klass.base_filters.update(cls.expand_auto_filter(klass, k, v))
            for k, v in klass.related_filters.items():
                klass.base_filters.update(cls.expand_auto_filter(klass, k, v))

        return klass

    @classmethod
    def get_auto_filters(cls, bases, attrs):
        auto_filters = [
            (k, attrs.pop(k))
            for k, v in attrs.copy().items()
            if isinstance(v, AutoFilter)
        ]

        for k, v in auto_filters:
            if getattr(v, 'field_name', None) is None:
                v.field_name = k

        auto_filters.sort(key=lambda x: x[1].creation_counter)

        for base in reversed(bases):
            if hasattr(base, 'auto_filters'):
                auto_filters = [
                    (k, v) for k, v in base.auto_filters.items() if k not in attrs
                ] + auto_filters

        return dict(auto_filters)

    @classmethod
    def expand_auto_filter(cls, new_class, filter_name, f):
        orig_meta = new_class._meta
        orig_declared = new_class.declared_filters
        new_class._meta = deepcopy(new_class._meta)
        new_class.declared_filters = {}
        new_class._meta.fields = {
            f.field_name: f.lookups or [],
        }

        d = {}
        for k, v in new_class.get_filters().items():
            k = k.replace(f.field_name, filter_name, 1)
            if k not in orig_declared:
                d[k] = v

        new_class._meta = orig_meta
        new_class.declared_filters = orig_declared
        return d


class SubsetDisabledMixin:
    @classmethod
    def get_filter_subset(cls, params, rel=None):
        return cls.base_filters


class FilterSet(_FilterSet, metaclass=FilterSetMetaclass):
    def __init__(self, data=None, queryset=None, *, relationship=None, **kwargs):
        self.base_filters = self.get_filter_subset(data or {}, relationship)
        super().__init__(data, queryset, **kwargs)
        self.relationship = relationship
        self.related_filtersets = self.get_related_filtersets()
        self.filters = self.get_request_filters()

    @classmethod
    def get_fields(cls):
        fields = super().get_fields()
        for k, v in fields.items():
            if v == '__all__':
                modelfield = get_model_field(cls._meta.model, k)
                if modelfield is not None:
                    fields[k] = lookups_for_field(modelfield)
                else:
                    fields[k] = []
        return fields

    @classmethod
    def get_filter_subset(cls, params, rel=None):
        names = {cls.get_param_filter_name(x, rel) for x in params}
        return {
            k: v for k, v in cls.base_filters.items() if k is not None and k in names
        }

    @classmethod
    def disable_subset(cls, *, depth=0):
        if not issubclass(cls, SubsetDisabledMixin):
            cls = type(f'SubsetDisabled{cls.__name__}', (SubsetDisabledMixin, cls), {})

        if depth > 0:
            cls.base_filters = cls.base_filters.copy()
            for name in cls.related_filters:
                filt = deepcopy(cls.base_filters[name])
                filt.filterset = filt.filterset.disable_subset(depth=depth - 1)
                cls.base_filters[name] = filt

        return cls

    @classmethod
    def get_param_filter_name(cls, param, rel=None):
        if not param:
            return param
        elif param == rel:
            return None

        prefix = '{}{}'.format(rel or '', LOOKUP_SEP)
        if rel and param.startswith(prefix):
            param = param[len(prefix) :]

        if param in cls.base_filters:
            return param
        elif param.endswith('!') and param[:-1] in cls.base_filters:
            return param[:-1]

        for filtername in sorted(cls.related_filters, reverse=True):
            if param.startswith(f'{filtername}{LOOKUP_SEP}'):
                return filtername
        return None

    def get_request_filters(self):
        d = {}
        for k, v in self.filters.items():
            d[k] = v
            if related(self, f'{k}!') in self.data:
                filt = deepcopy(self.base_filters[k])
                filt.parent = v.parent
                filt.model = v.model
                filt.exclude = not v.exclude
                d[f'{k}!'] = filt
        return d

    def get_related_filtersets(self):
        d = {}
        for k in self.related_filters:
            if k in self.filters:
                filt = self.filters[k]
                d[k] = filt.filterset(
                    data=self.data,
                    queryset=filt.get_queryset(self.request),
                    relationship=related(self, k),
                    request=self.request,
                    prefix=self.form_prefix,
                )
        return d

    def filter_queryset(self, queryset):
        return self.filter_related_filtersets(super().filter_queryset(queryset))

    def filter_related_filtersets(self, queryset):
        for k, v in self.related_filtersets.items():
            prefix = f'{related(self, k)}{LOOKUP_SEP}'
            if any(x.startswith(prefix) for x in self.data):
                paramname = LOOKUP_SEP.join([self.filters[k].field_name, 'in'])
                paramvalue = v.qs.values(
                    getattr(self.filters[k].field, 'to_field_name', 'pk') or 'pk'
                )
                queryset = queryset.filter(**{paramname: paramvalue})
                if self.related_filters[k].distinct:
                    queryset = queryset.distinct()
        return queryset

    def get_form_class(self):
        baseform = super().get_form_class()

        class Form(baseform):
            def add_prefix(form, field_name):
                return super().add_prefix(related(self, field_name))

            def clean(form):
                cleaned = super().clean()
                for v in self.related_filtersets.values():
                    for key, err in v.form.errors.items():
                        self.form.errors[related(v, key)] = err
                return cleaned

        return Form
