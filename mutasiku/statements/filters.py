import django_filters as filters
from .models import Statement


class StatementFilterSet(filters.FilterSet):
    class Meta:
        model = Statement
        fields = {
            "keterangan": ["icontains"]
        }
