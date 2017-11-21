from rest_framework.exceptions import ValidationError
from rest_framework.filters import BaseFilterBackend


class SearchFilter(BaseFilterBackend):
    search_form = None

    def filter_queryset(self, request, queryset, view):
        if hasattr(view, 'action') and view.action in getattr(view, 'search_action', ['list']):
            search_form = self.get_search_form(request, view)
            if search_form is not None:
                if not search_form.is_valid():
                    raise ValidationError(search_form.errors)
                queryset = search_form.search(queryset)
        return queryset

    def get_search_form(self, request, view):
        if self.search_form is None:
            search_form_class = getattr(view, 'search_form_class', None)
            if search_form_class is not None:
                kwargs = {'data': request.query_params}
                self.search_form = search_form_class(**kwargs)
        return self.search_form
