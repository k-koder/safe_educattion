# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.forms.models import model_to_dict
from django.contrib.auth import authenticate,login
error = False

def login(request):
    return render_to_response('login.html',{'error':error})

def auth(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    try :
        user=User.objects.get(username=username)
        if authenticate(username=username, password=password) is not None:
            return render_to_response('home.html',)
        else:
            error = True
            return render_to_response('login.html',{'error':error})
    except User.DoesNotExist:
        error = True
        return render_to_response('login.html',{'error':error})

def register(request):
    if not request.POST.get('username') :
               return render_to_response('register.html')
    else :
            username = request.POST.get('username')
            user=User.objects.filter(username=username)
            if user:
                error = True
                return render_to_response('register.html',{'error2': error})
            else :
                 password1 = request.POST.get('password1')
                 password2 = request.POST.get('password2')
                 email = request.POST.get('email')
                 if password1 == password2:
                     user = User.objects.create_user( username,email,password1)
                     return render_to_response('home.html')
                 else:
                    error = True
                    return render_to_response('register.html',{'error': error})

def home(request):
    return render_to_response('home.html')

