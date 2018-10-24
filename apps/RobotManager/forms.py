from django import forms

from apps.RobotManager.models import Project, Module, Cases, \
    Suites, Keyword, UserKeywords, Steps, Resource, CasesStep


class ProjectForm(forms.Form):
    project_type = (
        ('web', 'Web自动化'),
        ('app', 'App自动化'),
        ('inface', '接口自动化')
    )
    name = forms.CharField(
        required=True,
        empty_value='',
        error_messages={
            'required': '项目名称不能为空',
            'invalid': '请输入正确的测试名称'
        },
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '请输入项目名称'
            }
        ),
        label='项目名称',
        label_suffix=':'

    )
    creator = forms.CharField(label='创建人')
    type = forms.ChoiceField(choices=project_type, label='项目类型',
                             widget=forms.TextInput(
                                 attrs={
                                     'class': 'form-control',
                                     'placeholder': '请输入项目名称'
                                 }
                             ), )

    detail = forms.CharField(max_length=100, required=False,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control text-success', 'placeholder': '请输入备注'}),
                             label='备注')


class ModuleForm(forms.Form):
    project = Project.objects.all()
    project_list = []
    for p in project:
        t = []
        t.append(p.id)
        t.append(p.name)
        project_list.append(t)
    name = forms.CharField(
        required=True,
        empty_value='',
        error_messages={
            'required': '模块名称不能为空',
            'invalid': '请输入正确的模块名称'
        },
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '请输入模块名称'
            }
        ),
        label='模块名称',
        label_suffix=':'

    )
    belong_project = forms.IntegerField(
        widget=forms.Select(choices=tuple(project_list),
                            attrs={'class': 'selectpicker  bla bli form-control', 'data-live-search': 'true',
                                   'style': 'display: none'}), label='所属项目')
    detail = forms.CharField(max_length=100, required=False,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control text-success', 'placeholder': '请输入备注'}),
                             label='备注')


class SuiteForm(forms.Form):
    suite_num = forms.CharField(min_length=4, max_length=20, required=True, empty_value='',
                                error_messages={
                                    'required': '测试集编号不能为空',
                                    'invalid': '请输入4-20测试集编号',
                                },
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入测试编号'}),
                                label='测试集编号')

    name = forms.CharField(min_length=4, max_length=18, required=True, empty_value='',
                           error_messages={
                               'required': '名称不能为空'
                           },
                           widget=forms.TextInput(
                               attrs={'class': 'form-control text-success', 'placeholder': '请输入测试名称'}),
                           label='测试集名称')

    detail = forms.CharField(max_length=100, required=False,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control text-success', 'placeholder': '请输入备注'}),
                             label='备注')
