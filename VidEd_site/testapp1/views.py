import datetime

import django.contrib.auth
import pytz
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from datetime import *

from testapp1.models import Message

def index_page(request):
    return render(request, 'index.html')


def reg_page(request):
    return render(request, 'reg.html')

def newreg(request):
    if request.method == 'POST':
        print("\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("                         New register user!                            ")
        print("name: " + request.POST.__getitem__("name"))
        print("email: " + request.POST.__getitem__("email"))
        print("password: " + request.POST.__getitem__("password"))
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")

        user = User.objects.create_user(request.POST.__getitem__("name"), request.POST.__getitem__("email"), request.POST.__getitem__("password"))
        user.save()
        return render(request, 'regcomplete.html')

def auth_page(request):
    return render(request, 'auth.html')

def login_page(request):
    # if request.method =='POST':
    #     all_users = User.objects.all()
    #     for i in all_users:
    #         if i.get_username() == request.POST.__getitem__("NameOrEmail"):
    #             print("FIND!" + i.get_username())
    #             if i.acheck_password(request.POST.__getitem__("password")):
    #                 print("\n=============Success Authentication!!!=========")
    #                 print("Username (or email): " + request.POST.__getitem__("NameOrEmail"))
    #                 print("===============================================\n")
    #                 django.contrib.auth.login(request, i)
    #     print(request.session.items())
    #
    if request.method == 'POST':
        user = authenticate(username=request.POST.__getitem__("NameOrEmail"), password=request.POST.__getitem__("password"))
        if user is not None:
            login(request, user)
            print("\n=============Success Authentication!!!=========")
            print("Username (or email): " + request.user.get_username())
            print("===============================================\n")
            return HttpResponseRedirect("/profile/")

    return render(request, 'loginFailed.html')

def logout_page(request):
    print("\n===============Success Logout!!!===============")
    print("Username (or email): " + request.user.get_username())
    logout(request)
    print("To: " + str(request.user))
    print("===============================================\n")

    return HttpResponseRedirect("/index/")

def profile_page(request):
    return render(request, 'profile.html', {'name': request.user.get_username()})

def is_ajax(requset):
    return requset.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


@csrf_exempt
def messanger_page(request):
    if is_ajax(request) and request.method == 'POST':
        print(request.POST)
        if request.POST.get('text').find("WAIT_NEW_MESSAGES#") > -1:
            last_id = request.POST.get('text').split("WAIT_NEW_MESSAGES#")[1]
            tz = pytz.timezone("Etc/GMT-4")

            try:
                last_id = int(last_id)

                messages_to_send_text = []
                messages_to_send_date = []
                all_messages_for_refresh = ((Message.objects.filter(author=request.user.get_username()) & Message.objects.filter(
                                address=request.POST.get('address'))) |
                                (Message.objects.filter(author=request.POST.get('address')) & Message.objects.filter(
                                address=request.user.get_username())))
                for i in all_messages_for_refresh:

                    if i.id > last_id:
                        messages_to_send_text.append(i.text)
                        messages_to_send_date.append(tz.normalize(i.date.astimezone(tz)).strftime("%H:%M"))
                        last_id = i.id
                return JsonResponse({'text': messages_to_send_text, 'time': messages_to_send_date,
                                 'last_id': str(last_id)})
            except :
                pass
        else:
            new_message = Message(text=request.POST['text'], author=request.user.get_username(), address=request.POST.get('address'))
            new_message.save()
            return JsonResponse({'text': request.POST.get('text'), 'time': datetime.now().strftime("%H:%M"), 'last_id': str(new_message.id)})

    if request.method == 'GET':
        if request.GET.get('user') == None:
            return HttpResponseRedirect('/userlist/')
        all_messages = ((Message.objects.filter(author=request.user.get_username()) & Message.objects.filter(address=request.GET.get('user'))) |
                        (Message.objects.filter(author=request.GET.get('user')) & Message.objects.filter(address=request.user.get_username())))
        text_and_time = []
        tz = pytz.timezone("Etc/GMT-4")
        last_id = 0

        for i in all_messages:
            mess_date_utc4 = tz.normalize(i.date.astimezone(tz))                                    # Перевод времени в другой часовой пояс. ЭТО РАБОТАЕТ!
            if i.address == request.user.get_username():
                is_inner = True
            else:
                is_inner = False
            last_id = i.id
            text_and_time.append([i, mess_date_utc4.strftime("%H:%M"), is_inner])
        return render(request, 'messanger.html', {'username':request.GET.get('user'), 'text': text_and_time, 'last_id': last_id})



def userlist_page(request):
    all_users = User.objects.all()
    users_and_messages = []

    for user in all_users:
        user_messages = (Message.objects.filter(author=user) & Message.objects.filter(address=request.user)) | (Message.objects.filter(author=request.user) & Message.objects.filter(address=user))
        if len(user_messages) > 0 and user != request.user:
            last_message = user_messages[len(user_messages) - 1]
            users_and_messages.append([user.get_username(), last_message])
    print(users_and_messages)
    return render(request, 'userlist.html', {'data': users_and_messages})

def Design_page(request):
    return render(request, 'Design.html')

@csrf_exempt
def login_page(request):
    if is_ajax(request) and request.method == "POST":
        user = authenticate(username=request.POST.get("login"),
                            password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            print("\n=============Success Authentication!!!=========")
            print("Username (or email): " + request.user.get_username())
            print("===============================================\n")
            return JsonResponse({'text': 'NiceLogin'})
        else:
            return JsonResponse({'text': "NotLogin"})
    if request.method == "GET":
        return render(request, 'login.html')
def Prog_page(request):
    return render(request, 'Prog.html')
def VidEd_page(request):
    return render(request, 'VidEd.html')