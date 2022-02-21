from django.urls import reverse
from tokenize import group
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from chats.form import GroupData, GroupMessagesForm
from django.contrib.auth.decorators import login_required
from chats.models import GroupChat, GroupMessages
from django.contrib.auth.forms import UserCreationForm


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
    if request.POST:
        GroupMessages.objects.create(messages=message)
    msg_group = GroupMessagesForm()
    group_chat = group
    return render(request, 'chat/chatroom.html', {'group': group_chat, 'user': request.user,'msg_group': msg_group})

def get_data(request, num):
    # data = request.POST.get('messages')
    data = GroupMessages.objects.get(id=num)
    return JsonResponse({'messages': data.messages}, status=200)