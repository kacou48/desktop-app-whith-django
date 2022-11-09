from django.urls import path

from .views import (
    RoomListAPIView,
    RoomDetailAPIView,
    RoomUpdateAPIView,
    RoomDeleteAPIView,
    RoomCreateAPIView
)

app_name = 'todo-api'
urlpatterns = [

    path('', RoomListAPIView.as_view(), name='list'),
    path('create/', RoomCreateAPIView.as_view(), name='create'),
    path('<pk>/', RoomDetailAPIView.as_view(), name='detail'),
    path('<pk>/edit/', RoomUpdateAPIView.as_view(), name='update'),
    path('<pk>/delete/', RoomDeleteAPIView.as_view(), name='delete'),

]