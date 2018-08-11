from django import forms

from apps.RobotManager.models import Project,Module,Cases,\
    Suites,Keyword,UserKeywords,Steps,Resource,CasesStep


class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields='__all__'


class ModuleForm(forms.ModelForm):
    class Meta:
        model=Module
        fields='__all__'