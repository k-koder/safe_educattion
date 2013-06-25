# Create your views here.
from django.contrib.auth.models import User,AnonymousUser
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
            return render_to_response('home.html',{'user':user})
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
                     return render_to_response('home.html',{'user':user})
                 else:
                    error = True
                    return render_to_response('register.html',{'error': error})

def home(request):
    return render_to_response('home.html')
def user_manage(request):
   if  request.user.is_authenticated():
       return render_to_response('login.html')
   else:
       alluser = User.objects.all()
       return render_to_response('user_manage.html',{'Alluser':alluser})
def change_password(request):
    if not request.user.is_authenticated():
        return render_to_response('login.html')
    else :
        new_password = request.POST.get('password')
        user = User.objects.get(username__extct = request.user.username)
        user.set_password(new_password)
        user.save()
def delete_user(request):
    if  request.user.is_authenticated():
        return render_to_response('login.html')
    else :
        user = User.objects.get(username__exact = request.user.username)
        user.delete()
