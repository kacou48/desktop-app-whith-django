from rest_framework.serializers import(
    HyperlinkedIdentityField,
    ModelSerializer
)

from core.models import Room

class RoomCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'id',
            'room_num',
            'guest',
            'check_in',
            'check_out'

        ]

class RoomListSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'id',
            'room_num',
            'guest',
            'check_in',
            'check_out'

        ]


class RoomDetailSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'id',
            'room_num',
            'guest',
            'check_in',
            'check_out'

        ]