from django.shortcuts import render, redirect
from Problem.models import Problem
from Profile.models import Profile
from django.contrib import messages
import random

# Create your views here.
def home(request):
    data = {}
    try:
        data['problem'] = random.choice(Problem.objects.all())
    except :
        print("no problem")
    if request.user.is_authenticated:
        profile = Profile.objects.get(User=request.user)
        if profile.Code == "":
            data['can'] = True
        else: data['can'] = False
    return render(request, 'home2.html', data)

def save(request, username):
    if request.user.is_authenticated:
        if request.method == "POST":
            profile = Profile.objects.get(User=request.user)
            code = request.POST['code']
            if profile.Code == "":
                profile.Code = code
                profile.save()
            else:
                messages.error(request, "You have already submitted your code.")
    return redirect('home')    