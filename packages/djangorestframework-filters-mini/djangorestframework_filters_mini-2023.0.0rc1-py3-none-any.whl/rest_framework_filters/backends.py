from contextlib import contextmanager

from django_filters.rest_framework.backends import DjangoFilterBackend

from rest_framework_filters.filterset import FilterSet


class RestFrameworkFilterBackend(DjangoFilterBackend):
    filterset_base = FilterSet

    @property
    def template(self):
        return 'rest_framework_filters/form.html'

    @contextmanager
    def patch_for_rendering(self, request):
        original = self.get_filterset_class

        def get_filterset_class(view, queryset=None):
            klass = original(view, queryset)
            if klass is None:
                return None
            elif issubclass(klass, FilterSet):
                return klass.disable_subset(depth=1)
            else:
                return klass

        self.get_filterset_class = get_filterset_class
        try:
            yield
        finally:
            self.get_filterset_class = original

    def to_html(self, request, queryset, view):
        with self.patch_for_rendering(request):
            return super().to_html(request, queryset, view)
