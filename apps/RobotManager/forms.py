from django import forms

from apps.RobotManager.models import Project, Module, Cases, \
    Suites, Keyword, UserKeywords, Steps, Resource, CasesStep


class ProjectForm(forms.Form):
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

    type = forms.CharField(widget=forms.Select(choices=[],
                                               attrs={'class': 'selectpicker  bla bli form-control',
                                                      'data-live-search': 'true',
                                                      'style': 'display: none'}), label='项目类型')

    detail = forms.CharField(max_length=100,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control text-success', 'placeholder': '请输入备注'}),
                             label='备注')
    creator = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control", 'style': "display:None"}
    ), label=' ')

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['type'].widget.choices = Project.project_type


class ModuleForm(forms.Form):
    name = forms.CharField(
        required=True,
        empty_value='111',
        max_length=18,
        min_length=4,
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
        label_suffix=':'  # style="display: none"
        # readonly="readonly"

    )
    belong_project = forms.CharField(
        widget=forms.Select(choices=[],
                            attrs={'class': 'selectpicker  bla bli form-control', 'data-live-search': 'true',
                                   'style': 'display: none'}), empty_value='请选择', label='所属项目')
    detail = forms.CharField(max_length=100, required=False,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control text-success', 'placeholder': '请输入备注'}),
                             label='备注')

    def __init__(self, *args, **kwargs):
        super(ModuleForm, self).__init__(*args, **kwargs)
        self.fields['belong_project'].widget.choices = Project.objects.all().values_list('id', 'name')


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


class CaseForm(forms.Form):
    case_num = forms.CharField(max_length=20, required=True, label='用例编号',empty_value='111',
                               error_messages={
                                   'required': '用例编号不能为空',
                                   'invalid': '请重新输入用例编号'
                               },
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入测试编号'}),
                               )
    name = forms.CharField(max_length=20, required=True, label='用例标题',empty_value='111',
                           error_messages={
                               'required': '用例标题不能为空',
                               'invalid': '请重新输入用例标题'
                           },
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入测试编号'}),
                           )
    type = forms.CharField(widget=forms.Select(choices=[],
                                               attrs={'class': 'selectpicker  bla bli form-control',
                                                      'data-live-search': 'true',
                                                      'style': 'display: none'}), label='用例类型')
    level = forms.CharField(widget=forms.Select(choices=[],
                                                attrs={'class': 'selectpicker  bla bli form-control',
                                                       'data-live-search': 'true',
                                                       'style': 'display: none'}), label='优先级')

    def __init__(self, *args, **kwargs):
        super(CaseForm, self).__init__(*args, **kwargs)
        self.fields['type'].widget.choices = Cases.case_type
        self.fields['level'].widget.choices = Cases.case_level


