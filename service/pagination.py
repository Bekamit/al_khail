from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.utils.translation import get_language_from_request


class CustomPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = None
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            "language": get_language_from_request(self.request).upper(),
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'estates': list(data)
        }
        )
