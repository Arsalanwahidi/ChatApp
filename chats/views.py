from tokenize import group
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from chats.form import GroupData
from django.contrib.auth.decorators import login_required
from chats.models import GroupChat


# Create your views here.

@login_required(login_url='accounts/login/')
def home(request):
    
    group = GroupData(request.POST)
    
    if group.is_valid():
        group_data = group.cleaned_data['group']
        return render(request, 'chat/home.html', {'group': group})
    else:
        return render(request, 'chat/home.html', {'group': group})

def post_data(request):

    if request.method == 'POST':
        GroupChat.objects.create(group=request.POST.get('group'))
        return redirect('chat:home')


def get_data(request):

    data = GroupChat.objects.get(id=1)

    return JsonResponse({'data': data.group}, status=200)