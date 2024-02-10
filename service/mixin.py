from rest_framework import status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.response import Response

from apps.estate.models import Estate


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
        data = self.get_multilanguage_response(serializer)
        return Response(data)


class CustomSingletonListModelMixin:
    def first_list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset)
        data = self.get_multilanguage_response(serializer)
        return Response(data)


class CustomRetrieveMixin(RetrieveModelMixin):
    """
        Retrieve a queryset with custom Response.
        {
            "language": "EN",
            response_key: [serialize.data]
        }
    """

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if isinstance(instance, Estate):
            instance.visits_counter()

        serializer = self.get_serializer(instance)
        data = self.get_multilanguage_response(serializer)
        return Response(data)


class CustomCreateEstateMixin(CreateModelMixin):
    def create(self, request, *args, **kwargs):
        if kwargs.get('password') == 12345:
            return Response({
                "status": "ok",
                "estate": "created",
                "count": Estate.objects.all().count()
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "status": "error",
                "password": "is wrong",
            }, status=status.HTTP_400_BAD_REQUEST)
