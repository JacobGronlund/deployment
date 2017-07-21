from django.shortcuts import render, HttpResponse, redirect
from models import *
import time
import datetime
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'wall/index.html')
def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags = tag)
        return redirect(index)
    else:
        count = User.objects.filter(email = request.POST['email']).count()
        print count
        if count > 0:
            messages.error(request, 'email already used')
        else:
            hashedpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = hashedpw)
            b = User.objects.first()
        return redirect(index)

def check(request):
    user = User.objects.get(email = request.POST['email'])
    print user.password
    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        content = {
            'user': user
            }
        return render(request, 'wall/userwall.html', content)
    messages.error(request, 'incorrect password')
    return redirect(index)

def userwall(request):
    pass
        

