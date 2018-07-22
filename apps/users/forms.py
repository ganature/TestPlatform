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
    username=forms.CharField(max_length=8,required=True,label=u'用户名')
    password1=forms.CharField(required=True,max_length=8,label=u'密码')
    password2=forms.CharField(required=True,max_length=8,label=u'确认密码')

