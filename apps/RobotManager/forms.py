from django import forms

from apps.RobotManager.models import Project,Module,Cases,\
    Suites,Keyword,UserKeywords,Steps,Resource,CasesStep


class ProjectForm(forms.ModelForm):
    name=forms.CharField(
        required=True,
        empty_value='',
        error_messages={
            'required':'项目名称不能为空',
            'invalid':'请输入正确的测试名称'
        },
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'请输入项目名称'
            }
        ),
        label='项目名称',
        label_suffix=':'


    )


class ModuleForm(forms.ModelForm):
    class Meta:
        model=Module
        


class SuiteForm(forms.Form):
    suite_num = forms.CharField(min_length=4, max_length=20, required=True, empty_value='',
                                error_messages={
                                    'required': '测试集编号不能为空',
                                    'invalid': '请输入4-20测试集编号',
                                },
                                widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'请输入测试编号'}),
                                label='测试集编号')

    name = forms.CharField(min_length=4, max_length=18, required=True, empty_value='',
                           error_messages={
                                    'required': '名称不能为空'
                             },
                           widget=forms.TextInput(attrs={'class': 'form-control text-success','placeholder':'请输入测试名称'}),
                           label='测试集名称')

    detail=forms.CharField(max_length=100,required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control text-success','placeholder':'请输入备注'}),
                           label='备注')
