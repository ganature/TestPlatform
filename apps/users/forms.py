# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     forms
   Description :
   Author :       xudong_qiao
   date：          2018/7/21 0021
-------------------------------------------------
   Change Activity:
                   2018/7/21 0021:
-------------------------------------------------
"""
__author__ = 'xudong_qiao'

from django import forms





class RegisterForm(forms.Form):
    user_role = (
        (1,u'测试人员'),
        (2,u'开发人员')
    )
    username=forms.CharField(max_length=8,required=True,label=u'用户名')
    password1=forms.CharField(required=True,max_length=8,label=u'密码',widget=forms.PasswordInput)
    password2=forms.CharField(required=True,max_length=8,label=u'确认密码',widget=forms.PasswordInput)
    email=forms.EmailField(required=False,label=u'邮箱',widget=forms.EmailInput)
    role=forms.ChoiceField(choices=user_role,required=True,widget=forms.Select,label=u'职位',initial=1)
