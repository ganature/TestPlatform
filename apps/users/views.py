from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from users.forms import RegisterForm
from users.models import UserProfile


class RegisterView(View):


    def get(self,request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form': register_form})

    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name=request.POST.get('username')
            if UserProfile.objects.filter(username=user_name):
                return render(request,'register.html',{'msg':'用户名已存在'})
            pass_word=request.POST.get('password')
            user_profile=UserProfile()
            user_profile.username=user_name
            user_profile.password=pass_word
            user_profile.save()
