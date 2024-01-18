from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from django.utils.translation import get_language_from_request


class LimitOffsetCustomPagination(LimitOffsetPagination):

    def get_paginated_response(self, data):
        return Response({
            "language": get_language_from_request(self.request).upper(),
            'count': self.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'estates': data
        })

