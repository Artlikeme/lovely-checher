from rest_framework.generics import ListAPIView
from rest_framework import permissions

from .models import City
from .serializers import CitySerializer
from .services.get_user_city import get_user_city


class CityListView(ListAPIView):
    serializer_class = CitySerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        return City.objects.all().exclude(name=get_user_city(self.request))

    # def get_serializer_context(self):
    #     city = get_user_city(self.request)
    #     return city

    def list(self, request, *args, **kwargs):
        response = super().list(request, args, kwargs)
        city = City.objects.get(name=get_user_city(request))
        response.data.insert(0, {'your_city': {"id": city.id, "name": city.name}})

        return response

