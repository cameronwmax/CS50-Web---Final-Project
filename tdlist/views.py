import json
import datetime as dt
from django.utils import timezone
import datetime
from django.http import JsonResponse
from django.shortcuts import render
from django.db import IntegrityError
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect

from .models import User, List

# Create your views here.
def index(request):
    return render(request, "tdlist/index.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "tdlist/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "tdlist/register.html")
    

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "tdlist/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "tdlist/login.html")
    

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def create_list(request):
    if request.method == "POST":
        list_content = request.POST['list_content']
        user = User.objects.get(pk=request.user.id)

        
        today = datetime.datetime.now() #dt.datetime.now(tz=timezone.UTC)

        new_list = List(list_content=list_content, user=user, date_created=today)
        new_list.save()
        return HttpResponseRedirect(reverse(my_list))
    return render(request, "tdlist/create_list.html")


def my_list(request):
    user = User.objects.get(pk=request.user.id)
    all_lists = List.objects.filter(user=user).order_by("id").reverse()
    return render(request, "tdlist/my_list.html", {
        "all_lists": all_lists,
        "amount": len(all_lists),
    })


def delete_list(request, list_id):
    if request.method == "POST":
        del_list = List.objects.get(pk=list_id)
        del_list.delete()
        return HttpResponseRedirect(reverse(my_list))


def delete_all(request):
    user = User.objects.get(pk=request.user.id)
    all_lists = List.objects.filter(user=user).order_by("id").reverse()
    for item in all_lists:
        item.delete()
    return HttpResponseRedirect(reverse(my_list))


def edit_task(request, list_id):
    task = List.objects.get(pk=list_id)
    new_task = request.POST.get('new-task-content')
    task.list_content = new_task
    print(task)
    task.save()
    return HttpResponseRedirect(reverse(my_list))