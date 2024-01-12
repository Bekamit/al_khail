from django_filters import rest_framework as filters
from .models import Estate


class EstateFilter(filters.FilterSet):
    ordering = filters.OrderingFilter(
        fields=(
            ('-create_at', '-create_at'),  # Сортировка по дате создания (возрастание)
            ('visits', 'visits'),  # Сортировка по количеству посещений (убывание)
        ),
    )

    class Meta:
        model = Estate
        fields = ['city_id', 'estate_type_id', 'is_secondary', 'project_id']
