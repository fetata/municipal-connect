from django.db.models import Q


class SearchMixin:
    search_fields = []

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")

        if query and self.search_fields:
            q_objects = Q()

            for field in self.search_fields:
                q_objects |= Q(**{f"{field}__icontains": query})

            queryset = queryset.filter(q_objects)

        return queryset
