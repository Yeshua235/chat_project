from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ChatRoom, Message

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ChatRoomListView(LoginRequiredMixin, ListView):
    model = ChatRoom
    template_name = 'chatroom_list.html'
    context_object_name = 'chatrooms'

class ChatRoomDetailView(LoginRequiredMixin, DetailView):
    model = ChatRoom
    template_name = 'chatroom_detail.html'
    context_object_name = 'chatroom'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Message.objects.filter(room=self.get_object())
        return context

