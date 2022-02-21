from django.urls import path
from chats import views

app_name = 'chat'

urlpatterns = [
    path('chat', views.home, name='home'),
    path('postdata/<str:group>', views.post_data, name='post'),
    path('getdata/<int:num>', views.get_data, name='get'),
    path('check_group', views.check_group, name='checkGroup'),
]