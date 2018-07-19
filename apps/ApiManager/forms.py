#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2018年6月30日

@author: neildian
'''
from django import forms


class AddProjectForm (forms.Form):
    project_name = forms.CharField ()
    responsible_name = forms.CharField ()
    test_user = forms.CharField ()
    dev_user = forms.CharField ()
    publish_app = forms.CharField ()
    simple_desc = forms.CharField ()
    other_desc = forms.CharField ()


class AddModuleForm (forms.Form):
    module_name = forms.CharField ()
    belong_project = forms.CharField ()
    test_user = forms.CharField ()
    simple_desc = forms.CharField ()
    other_desc = forms.CharField ()


class AddApiInfoForm (forms.Form):
    belong_project = forms.CharField (required=False)
    belong_module = forms.CharField (required=False)
    apiname = forms.CharField (required=False)
    httpType = forms.CharField (required=False)
    requestType = forms.CharField (required=False)
    apiAddress = forms.CharField (required=False)
    requestParameterType = forms.CharField (required=False)
    description = forms.CharField (required=False)