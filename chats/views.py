from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from jinja2_time import TimeExtension
from chats.form import GroupData, GroupMessagesForm
from django.contrib.auth.decorators import login_required
from chats.models import GroupChat, GroupMessages
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

# Create your views here.

@login_required(login_url='accounts/login/')
def home(request):
    
    group = GroupData(request.POST)

    if group.is_valid():
        return render(request, 'chat/home.html', {'group': group})
    else:
        return render(request, 'chat/home.html', {'group': group})

def check_group(request):
    group_data = GroupData(request.POST)
    
    if group_data.is_valid():
        check_group = group_data.cleaned_data['group']
        group_chat = GroupChat.objects.filter(group=check_group).exists()
        if group_chat:
            return redirect(reverse('chat:post', args=(check_group,)))
        else:
            GroupChat.objects.create(group=request.POST.get('group'))
            return redirect(reverse('chat:post', args=(check_group,)))
    else:
        return HttpResponse("<h1 style='text-align: center; margin-top: 50px'>Request Not Process Successfully</h1>")

def post_data(request, group):

    message = request.POST.get('messages')
    user = request.POST.get('user')
    # date = request.POST.get('date')

    if request.POST:
        GroupMessages.objects.create(messages=message, user=user, date=datetime.now())
    msg_group = GroupMessagesForm()
    group_chat = group
    return render(request, 'chat/chatroom.html', {'group': group_chat, 'user': request.user,'msg_group': msg_group, 'd': datetime.now().time()})

def get_data(request, num):
    
    data = GroupMessages.objects.filter(id=num)
    return JsonResponse({'messages': list(data.values())}, status=200)