from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from rest_framework import mixins
from rest_framework import viewsets
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.views import View
from django.urls import reverse
from django.shortcuts import redirect
from apps.RobotManager.serializers import ProjectSerializer, ModuleSerializer, SuitesSerializer, \
    KeywordSerializer, UserKeywordsSerializer, CasesSerializer, CasesStepSerializer, StepswordsSerializer
import json

# Create your views here.
from apps.users.models import UserProfile

from apps.users.models import UserProfile
from apps.RobotManager.models import Project, Module, Cases, \
    Suites, Keyword, UserKeywords, Steps, Resource, CasesStep
from apps.RobotManager.forms import ProjectForm, SuiteForm, ModuleForm, CaseForm
from django.core.paginator import Paginator


def get_pages(totalpage=1, current_page=1):
    """
    example: get_pages(10,1) result=[1,2,3,4,5]
    example: get_pages(10,9) result=[6,7,8,9,10]
    页码个数由WEB_DISPLAY_PAGE设定
    分页
    """
    WEB_DISPLAY_PAGE = 5
    front_offset = int(WEB_DISPLAY_PAGE / 2)
    if WEB_DISPLAY_PAGE % 2 == 1:
        behind_offset = front_offset
    else:
        behind_offset = front_offset - 1

    if totalpage < WEB_DISPLAY_PAGE:
        return list(range(1, totalpage + 1))
    elif current_page <= front_offset:
        return list(range(1, WEB_DISPLAY_PAGE + 1))
    elif current_page >= totalpage - behind_offset:
        start_page = totalpage - WEB_DISPLAY_PAGE + 1
        return list(range(start_page, totalpage + 1))
    else:
        start_page = current_page - front_offset
        end_page = current_page + behind_offset
        return list(range(start_page, end_page + 1))


class ProjectView(View):
    """
    项目列表页
    """

    def get(self, request):
        project_form = ProjectForm()
        project = Project.objects.all()
        search_keyword = request.GET.get('project_name')
        search_type = request.GET.get('project_type')
        print(search_type)
        search_dict = {}
        if search_keyword:
            search_dict['name'] = search_keyword
        if search_type:
            search_dict['type'] = search_type
        # if search_keyword:
        #     project = Project.objects.filter(name__contains=search_keyword,type__contains=search_type)
        project = Project.objects.filter(**search_dict)
        # print(Project)

        paginator_obj = Paginator(project, 10)  # 每页10条
        request_page_num = request.GET.get('page', 1)
        project_obj = paginator_obj.page(request_page_num)

        total_page_number = paginator_obj.num_pages

        project_list = get_pages(int(total_page_number), int(request_page_num))

        return render(request, 'robotTemplates/robot_project_list.html',
                      {'obj': project_obj, 'obj_list': project_list, 'obj_form': project_form})


class ProjectEditView(View):
    """
    项目编辑页
    """

    def get(self, request, id):
        project = Project.objects.get(id=id)

        user = UserProfile.objects.get(username=project.creator)

        project_form = ProjectForm(
            {'name': project.name,
             'type': project.type,
             'creator': user.username,
             'detail': project.detail}
        )
        return render(request, 'robotTemplates/robot_project_edit.html', {'obj_form': project_form})

    def post(self, request, id):
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project = Project.objects.get(id=id)
            project.name = request.POST['name']
            project.type = request.POST['type']
            project.detail = request.POST['detail']
            project.creator = UserProfile.objects.get(username=request.user)
            project.save()
        return HttpResponseRedirect(reverse('project_list'))


class ProjectAddView(View):
    """
    项目新增页面
    """

    def get(self, request):

        user = UserProfile.objects.get(username=request.user)

        project_form = ProjectForm(
            {'creator': user.username}
        )

        return render(request, 'robotTemplates/robot_project_add.html', {'obj_form': project_form})

    def post(self, request):
        project_form = ProjectForm(request.POST)

        if project_form.is_valid():
            name = request.POST['name']
            type = request.POST['type']
            detail = request.POST['detail']
            creator = UserProfile.objects.get(username=request.user)
            project = Project(name=name, type=type, detail=detail, creator=creator)
            project.save()
        else:
            return render(request, 'robotTemplates/robot_project_add.html', {'error': project_form.errors})
        return HttpResponseRedirect(reverse('project_list'))


class ModuleView(View):
    """
    模块列表页面
    """

    def get(self, request):
        project_list = Project.objects.all()
        search_keyword = request.GET.get('module_name')
        search_project = request.GET.get('project')

        search_dict = {}
        if search_keyword:
            search_dict['name'] = search_keyword
        if search_project:
            p = Project.objects.get(name=search_project)
            search_dict['belong_project'] = p.id

        module = Module.objects.filter(**search_dict)
        paginator_obj = Paginator(module, 10)  # 每页10条
        request_page_num = request.GET.get('page', 1)
        module_obj = paginator_obj.page(request_page_num)

        total_page_number = paginator_obj.num_pages

        module_list = get_pages(int(total_page_number), int(request_page_num))

        return render(request, 'robotTemplates/robot_module_list.html',
                      {'obj': module_obj, 'obj_list': module_list, 'project_list': project_list})


class ModuleAddView(View):
    """
    模块/包新增页面
    """

    def get(self, request):

        module_form = ModuleForm()
        return render(request, 'robotTemplates/robot_module_add.html', {'obj_form': module_form})

    def post(self, request):
        module_form = ModuleForm(request.POST)
        if module_form.is_valid():
            name = request.POST['name']
            belong_project = Project.objects.get(id=request.POST['belong_project'])
            creator = UserProfile.objects.get(username=request.user)
            detail = request.POST['detail']
            module = Module(name=name, belong_project=belong_project, creator=creator, detail=detail)
            module.save()
        else:
            return render(request, 'robotTemplates/robot_module_add.html', {'error': module_form.errors})
        return HttpResponseRedirect(reverse('module_list'))


class ModuleListView(View):
    """
    模块列表
    """

    def get(self, request):
        module = Module.objects.all()
        return render(request, 'robotTemplates/robot_module_list.html', {'obj': module})


class ModuleEditView(View):
    def get(self, request, id):
        module = Module.objects.get(id=id)
        m = Module.objects.filter(id=id)
        project_name = Project.objects.get(id=module.belong_project_id)
        obj_form = ModuleForm({
            'name': module.name,
            'belong_project': project_name.id,
            'detail': module.detail
        })

        return render(request, 'robotTemplates/robot_module_edit.html', {'obj_form': obj_form})

    def post(self, request, id):
        module_form = ModuleForm(request.POST)
        if module_form.is_valid():
            module = Module.objects.get(id=id)
            module.name = request.POST['name']
            module.belong_project = Project.objects.get(request.POST['belong_project'])
            module.detail = module_form.cleaned_data['detail']
            module.save()


class CaseListView(View):
    """
    用例模块列表视图
    """

    def get(self, request):
        case_form = CaseForm()
        project_list = Project.objects.all()

        case = Cases.objects.all()
        paginator_obj = Paginator(case, 10)  # 每页10条
        request_page_num = request.GET.get('page', 1)
        case_obj = paginator_obj.page(request_page_num)

        total_page_number = paginator_obj.num_pages

        case_list = get_pages(int(total_page_number), int(request_page_num))

        return render(request, 'robotTemplates/robot_case_list.html',
                      {'obj': case_obj, 'obj_list': case_list, 'project_list': project_list, 'obj_form': case_form})


class CaseAddView(View):
    """
    用例新增视图
    """

    def get(self, request):
        case_form = CaseForm()
        # print(case_form)
        # print(type(case_form))
        return render(request, 'robotTemplates/robot_case_add.html', {'obj_form': case_form})

    def post(self, request):
        case_form = CaseForm(request.POST)
        user = UserProfile.objects.get(username=request.user)
        if case_form.is_valid():
            case_num = request.POST['case_num']
            name = request.POST['name']
            type = request.POST['type']
            level = request.POST['level']
            creator = user
            case = Cases(case_num=case_num, name=name, type=type, level=level, creator=creator)
            case.save()
            # return render(request,'robotTemplates/robot_case_list.html',{'error_code':100,'msg': '保存成功'})
            return HttpResponse(json.dumps({'error_code':100,'error_msg':"保存成功"}))
        return render(request, 'robotTemplates/robot_case_list.html')


class CaseEditView(View):
    """
    用例编辑视图
    """

    def get(self, request, id):
        case = Cases.objects.get(id=id)
        case_form = CaseForm({
            'case_num': case.case_num,
            'name': case.name,
            'type': case.type,
            'level': case.level
        }
        )
        return render(request, 'robotTemplates/robot_case_edit.html', {'obj_form': case_form})

    def post(self, request):
        case_form = CaseForm(request.POST)
        user = UserProfile.objects.get(username=request.user)
        if case_form.is_valid():
            case_num = request.POST['case_num']
            name = request.POST['name']
            type = request.POST['type']
            level = request.POST['level']
            creator = user.username
            case = Cases(case_num=case_num, name=name, type=type, level=level, creator=creator)
            case.save()
            return HttpResponse({'msg': '保存成功'})
        return render(request, 'robotTemplates/robot_case_list.html')


class SuiteAddView(View):
    """
    测试集新增页
    """

    @staticmethod
    def get(request):
        suiteform = SuiteForm()
        return render(request, 'robotTemplates/robot_suite_add.html', {'obj_form': suiteform})

    @staticmethod
    def post(request):
        suiteform = SuiteForm(request.POST)
        if suiteform.is_valid():
            suiteform.save(commit=True)
            return render(request, 'robotTemplates/robot_suite_list.html', {'msg': '保存成功'})
        else:
            error = suiteform.errors
            return render(request, 'robotTemplates/robot_suite_add.html', {'suiteform': suiteform, 'error': error})


class SuiteListView(View):
    """
    测试集列表页
    """

    @staticmethod
    def get(request):
        suite = Suites.objects.all()
        paginator_obj = Paginator(suite, 10)
        request_page_num = request.GET.get('page', 1)
        suite_obj = paginator_obj.page(request_page_num)
        total_page_number = paginator_obj.num_pages
        suite_list = get_pages(int(total_page_number), int(request_page_num))

        return render(request, 'robotTemplates/robot_suite_list.html', {'obj': suite_obj, 'obj_list': suite_list})


class SuiteEditView(View):
    """
    测试集编辑视图
    """
