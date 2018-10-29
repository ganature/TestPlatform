# coding=utf-8

import xadmin

from apps.RobotManager.models import Project,Module,Cases,Suites,Steps \
    ,CasesStep,Library,Keyword,UserKeywords,Resource


class ProjectAdmin(object):
    list_display = ['name','type','creator','detail','remark','add_time','edit_time']
    search_fields = ['name','type','creator']
    list_filter = ['name','type','creator']


class ModuleAdmin(object):
    list_display = ['name','belong_project','creator','detail','remark','add_time','edit_time']
    search_fields = ['name','belong_project','creator']
    list_filter = ['name','belong_project','creator']


class CasesAdmin(object):
    list_display = ['case_num','name','type','creator','suite','expect','level','detail','remark','add_time',
                    'edit_time']
    search_fields = ['case_num','name','suite','creator','level']
    list_filter = ['case_num','name','suite','creator','level']


class SuitesAdmin(object):
    list_display = ['suite_num','name','belong_module','creator','detail','remark','add_time','edit_time']
    search_fields = ['suite_num','name','belong_module','creator']
    list_filter = ['suite_num','name','belong_module','creator']


class CasesStepAdmin(object):
    list_display = ['case_id','step_seqnum','step_id','add_time','edit_time']
    search_fields = ['case_id','step_seqnum','step_id']
    list_filter = ['case_id','step_seqnum','step_id']


class StepsAdmin(object):
    list_display = ['step_num','name','keyword','doc','add_time','edit_time']
    search_fields = ['step_num','name','keyword','doc']
    list_filter = ['step_num','name','keyword','doc']


class LibraryAdmin(object):
    list_display = ['name','doc','add_time','edit_time']
    search_fields = ['name','doc']
    list_filter = ['name','doc']


class KeywordAdmin(object):
    list_display = ['name','doc','library','add_time','edit_time']
    search_fields = ['name','doc','library']
    list_filter = ['name','doc','library']


class ResourceAdmin(object):
    list_display = ['name','doc','module','add_time','edit_time']
    search_fields = ['name','doc','module']
    list_filter = ['name','doc','module']


class UserKeywordsAdmin(object):
    list_display = ['name','doc','resource','add_time','edit_time']
    search_fields = ['name','doc','resource']
    list_filter = ['name','doc','resource']


xadmin.site.register(Project,ProjectAdmin)
xadmin.site.register(Module,ModuleAdmin)
xadmin.site.register(Cases,CasesAdmin)
xadmin.site.register(Suites,SuitesAdmin)
xadmin.site.register(Steps,StepsAdmin)
xadmin.site.register(CasesStep,CasesStepAdmin)
xadmin.site.register(Library,LibraryAdmin)
xadmin.site.register(Keyword,KeywordAdmin)
xadmin.site.register(UserKeywords,UserKeywordsAdmin)
xadmin.site.register(Resource,ResourceAdmin)
