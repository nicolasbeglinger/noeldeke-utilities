from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('chat', views.chat, name='chat'),
    path('', RedirectView.as_view(url='chat'))
]
