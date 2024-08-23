from django.urls import path
from .views import ChatRoomListView, ChatRoomDetailView

urlpatterns = [
    path('', ChatRoomListView.as_view(), name='chatroom_list'),
    path('<int:pk>/', ChatRoomDetailView.as_view(), name='chatroom_detail'),
]
