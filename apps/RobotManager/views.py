from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from rest_framework import mixins
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
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
from apps.RobotManager.models import Project, Module, Cases, \
    Suites, Keyword, UserKeywords, Steps, Resource, CasesStep
from apps.RobotManager.forms import ProjectForm, SuiteForm, ModuleForm
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
        for p in project:
            print(p.add_time)
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
        return render(request, 'robotTemplates/robot_project_edit.html', {'project': project})

    def post(self, request):
        project_form = ProjectForm(request)
        if project_form.is_valid():
            project_form.save()
        return render(request, 'project_list.html')


class ProjectAddView(View):
    """
    项目新增页面
    """

    def get(self, request):
        return render(request, 'robotTemplates/robot_project_add.html')

    def post(self, request):
        project_form = ProjectForm(request.POST)
        print(request.POST)
        # project_form.creator=request.POST['creator']
        if project_form.is_valid():
            project_form.save()
        else:
            return render(request, 'robotTemplates/robot_project_add.html', {'error': project_form.errors})
        return HttpResponseRedirect(reverse('project_list'))


class ModuleView(View):
    """
    模块列表页面
    """

    def get(self, request):
        module_form = ModuleForm()
        module = Module.objects.all()
        paginator_obj = Paginator(module, 10)  # 每页10条
        request_page_num = request.GET.get('page', 1)
        module_obj = paginator_obj.page(request_page_num)

        total_page_number = paginator_obj.num_pages

        module_list = get_pages(int(total_page_number), int(request_page_num))

        return render(request, 'robotTemplates/robot_module_list.html',
                      {'obj': module_obj, 'obj_list': module_list, 'obj_form': module_form})


class ModuleAddView(View):
    """
    模块/包新增页面
    """

    @staticmethod
    def get(request):
        return render(request, 'robotTemplates/robot_module_add.html')

    @staticmethod
    def post(request):
        module_form = ModuleForm(request.POST)
        if module_form.is_valid():
            module_form.save()
        else:
            return render(request, 'robotTemplates/robot_module_add.html', {'error': module_form.errors})
        return HttpResponseRedirect(reverse('module_list'))


class SuiteAddView(View):
    """
    测试集新增页
    """

    @staticmethod
    def get(request):
        suiteform = SuiteForm()
        return render(request, 'robotTemplates/robot_suite_add.html', {'suiteform': suiteform})

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
