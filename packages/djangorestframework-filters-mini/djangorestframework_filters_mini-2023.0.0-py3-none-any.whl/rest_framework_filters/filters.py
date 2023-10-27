from django.utils.module_loading import import_string
from django_filters.filters import (  # unused; only for backwards-compatibility
    AllValuesFilter,
    AllValuesMultipleFilter,
    BaseCSVFilter,
    BaseInFilter,
    BaseRangeFilter,
    CharFilter,
    ChoiceFilter,
    DateFilter,
    DateFromToRangeFilter,
    DateRangeFilter,
    DateTimeFilter,
    DateTimeFromToRangeFilter,
    DurationFilter,
    Filter,
    IsoDateTimeFilter,
    IsoDateTimeFromToRangeFilter,
    LookupChoiceFilter,
    MultipleChoiceFilter,
    NumberFilter,
    NumericRangeFilter,
    OrderingFilter,
    RangeFilter,
    TimeFilter,
    TimeRangeFilter,
    TypedChoiceFilter,
    TypedMultipleChoiceFilter,
    UUIDFilter,
)
from django_filters.rest_framework.filters import (  # for backwards-compatibility
    BooleanFilter,
)
from django_filters.rest_framework.filters import (
    ModelChoiceFilter,
    ModelMultipleChoiceFilter,
)

__all__ = (
    'AllValuesFilter',
    'AllValuesMultipleFilter',
    'BaseCSVFilter',
    'BaseInFilter',
    'BaseRangeFilter',
    'CharFilter',
    'ChoiceFilter',
    'DateFilter',
    'DateFromToRangeFilter',
    'DateRangeFilter',
    'DateTimeFilter',
    'DateTimeFromToRangeFilter',
    'DurationFilter',
    'Filter',
    'IsoDateTimeFilter',
    'IsoDateTimeFromToRangeFilter',
    'LookupChoiceFilter',
    'MultipleChoiceFilter',
    'NumberFilter',
    'NumericRangeFilter',
    'OrderingFilter',
    'RangeFilter',
    'TimeFilter',
    'TimeRangeFilter',
    'TypedChoiceFilter',
    'TypedMultipleChoiceFilter',
    'UUIDFilter',
    'BooleanFilter',
    'ModelChoiceFilter',
    'ModelMultipleChoiceFilter',
    'AutoFilter',
    'BaseRelatedFilter',
    'RelatedFilter',
    'RelatedMultipleFilter',
)


class AutoFilter:
    creation_counter = 0

    def __init__(self, field_name=None, *, lookups=None):
        self.field_name = field_name
        self.lookups = lookups or []
        self.creation_counter = AutoFilter.creation_counter
        AutoFilter.creation_counter += 1


class BaseRelatedFilter:
    def __init__(self, filterset, *args, lookups=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.filterset = filterset
        self.lookups = lookups or []

    def bind_filterset(self, filterset):
        if not hasattr(self, 'bound_filterset'):
            self.bound_filterset = filterset

    def filterset():
        def fget(self):
            if isinstance(self._filterset, str):
                try:
                    self._filterset = import_string(self._filterset)
                except ImportError:
                    self._filterset = import_string(
                        '.'.join([self.bound_filterset.__module__, self._filterset])
                    )
            return self._filterset

        def fset(self, value):
            self._filterset = value

        return locals()

    filterset = property(**filterset())

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if queryset is None:
            clsname = type(self.parent).__name__
            fldname = self.field_name
            raise AssertionError(
                f"Expected `.get_queryset()` for related filter '{clsname}.{fldname}' "
                'to return a `QuerySet`, but got `None`.'
            )
        return queryset


class RelatedFilter(BaseRelatedFilter, ModelChoiceFilter):
    pass


class RelatedMultipleFilter(BaseRelatedFilter, ModelMultipleChoiceFilter):
    pass
