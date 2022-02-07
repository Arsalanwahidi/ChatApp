from django.urls import path
from chats import views

app_name = 'chat'

urlpatterns = [
    path('chat', views.home, name='home'),
    path('postdata', views.post_data, name='post'),    
    path('getdata', views.get_data, name='get'),
]