from django import forms

from apps.RobotManager.models import Project,Module,Cases,\
    Suites,Keyword,UserKeywords,Steps,Resource,CasesStep


class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields='__all__'
        labels={
            'name':'项目名称',
            'type':'项目类型',
            'creator':'创建人',
            'detail':'项目描述',
            'addtime':'创建时间',
            'edittime':'修改时间',
        }


class ModuleForm(forms.ModelForm):
    class Meta:
        model=Module
        fields='__all__'

class SuiteForm(forms.ModelForm):
    # suite_num=forms.CharField(min_length=4,max_length=20,required=True,empty_value=u'请输入4-20测试集编号',error_messages={
    #     'required':'测试集编号不能为空',
    #     'invalid':'请输入4-20测试集编号',
    # },widget=forms.TextInput(attrs={'class':'form-contrl'}),label='编号')
    # name=forms.CharField(min_length=4,max_length=18,required=True,empty_value='请输入4-20测试集编号',error_messages={
    #     'required':'名称不能为空'
    # },widget=forms.TextInput(attrs={'class':'form-contrl'}),label='测试集名称')
    class Meta:
        model=Suites
        fields='__all__'
        widgets={
            'belong_module':forms.Select(attrs={'class':'selectpicker'}),

        }