from django.core.validators import EMPTY_VALUES


class SearchFormMixin:
    def search(self, queryset):
        queries = []

        for key, value in self.cleaned_data.items():
            if hasattr(self, 'search_{}'.format(key)) and value not in EMPTY_VALUES:
                query = getattr(self, 'search_{}'.format(key))(value)
                if query:
                    queries.append(query)
        return queryset.filter(*queries)
