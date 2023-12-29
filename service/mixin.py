from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response


class CustomListModelMixin(ListModelMixin):
    """
    List a queryset with custom Response.
    {
        language: 'EN',
        response_key: [serialize.data]
    }
    """

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        response_key = self.get_response_key()
        if response_key:
            language = self.get_response_language()
            data = {
                "language": language,
                response_key: serializer.data
            }
        else:
            data = serializer.data
        return Response(data)
