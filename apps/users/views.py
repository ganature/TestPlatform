from django.shortcuts import render,HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.urls import reverse
from apps.users.forms import RegisterForm
from apps.users.models import UserProfile
from rest_framework import mixins
from rest_framework import viewsets
from apps.users.serializers import UserProfileSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters






class UserProfileViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    serializer_class = UserProfileSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class RegisterView(View):


    def get(self,request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form': register_form})

    def post(self,request):
        user_name=request.POST.get('username')
        if UserProfile.objects.filter(username=user_name):
            return render(request,'register.html',{'msg':'用户名已存在','status_code':999})
        else:
            pass_word=request.POST.get('password1')
            user_profile=UserProfile()
            user_profile.username=user_name
            user_profile.password=pass_word
            user_profile.save()
            return render(request,'index.html',{'status_code':100,'msg':'用户保存成功'})

class LoginView(View):

    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        name=request.COOKIES.get('name')
        if name:
            return render(request,'robotTemplates/index.html')
        user_name=request.POST.get('username')
        pass_word = request.POST.get('password')
        auth_login=authenticate(username=user_name,password=pass_word)
        print(auth_login)
        if auth_login :
            login(request,auth_login)
            response=HttpResponseRedirect('/robot_project_list/')
            response.set_cookie('name',user_name,60*60*24*1)
            return response
        else:
            return render(request,'login.html',{'msg':'登录失败','status_code':101})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))



