from rest_framework import status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.response import Response

from apps.staticdata.models import DefaultValue
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


class CustomSingletonListModelMixin(ListModelMixin):
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
            if len(serializer.data) == 1:
                data = {
                    "language": language,
                    response_key: serializer.data[0]
                }
            else:
                data = {
                    "language": language,
                    response_key: serializer.data
                }
        else:
            data = serializer.data
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


class CustomRetrieveEstateImageMixin(ListModelMixin):
    """
        List a image queryset with custom Response.
        {
            "estate_id": estate_id,
            "images": [absolute_url/image1.jpg, absolute_url/image2.jpg, ...]
        }
    """

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        response = {"estate_id": self.kwargs.get('id')}
        current_host = request.get_host()

        data = []
        if queryset:
            for image in queryset:
                data.append(f"{request.scheme}://{current_host}{image.img.url}")
        else:
            try:
                data.append(f"{request.scheme}://{current_host}{DefaultValue.default_img().url}")
            except:
                data.append('No Image')
        response["images"] = data

        serializer = self.get_serializer(response)
        return Response(serializer.data)


class CustomCreateEstateMixin(CreateModelMixin):
    def create(self, request, *args, **kwargs):
        return Response({
            "status": "ok",
            "estate": "created",
            "count": Estate.objects.all().count()
        }, status=status.HTTP_201_CREATED)
