from django.db.models import Q
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    CreateAPIView
)

from core.models import Room
from .serializers import (
    RoomListSerializer,
    RoomDetailSerializer,
    RoomCreateUpdateSerializer
)

class RoomCreateAPIView(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomCreateUpdateSerializer


class RoomDetailAPIView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer
    lookup_field = 'pk'


class RoomUpdateAPIView(UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer
    lookup_field = 'pk'

    #lookup_url_kwarg = "abc"

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class RoomDeleteAPIView(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer
    lookup_field = 'pk'


class RoomListAPIView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer
