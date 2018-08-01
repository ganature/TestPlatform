#coding=utf-8

import xadmin

from apps.RobotManager.models import Project,Module,Cases,Suites,Steps,CasesStep

class ProjectAdmin(object):
    list_display=['name','type','creator','detail','remark','add_time','edit_time']
    search_fields=['name','type','creator']
    list_filter=['name','type','creator']

class ModuleAdmin(object):
    list_display = ['name', 'belong_project', 'creator', 'detail', 'remark', 'add_time', 'edit_time']
    search_fields = ['name', 'belong_project', 'creator']
    list_filter = ['name', 'belong_project', 'creator']

class CasesAdmin(object):
    list_display = ['case_num','name', 'type', 'creator','suite','expect','level' 'detail', 'remark', 'add_time', 'edit_time']
    search_fields = ['case_num','name', 'suite', 'creator','level']
    list_filter = ['case_num','name', 'suite', 'creator','level']

class SuitesAdmin(object):
    list_display = ['suite_num','name', 'belong_module', 'creator', 'detail', 'remark', 'add_time', 'edit_time']
    search_fields = ['suite_num','name', 'belong_module', 'creator']
    list_filter = ['suite_num','name', 'belong_module', 'creator']

class CasesStepAdmin(object):
    list_display = ['case_id', 'step_seqnum', 'step_id', 'add_time', 'edit_time']
    search_fields = ['case_id', 'step_seqnum', 'step_id']
    list_filter = ['case_id', 'step_seqnum', 'step_id']

class StepsAdmin(object):
    list_display = ['step_num', 'name', 'step_id', 'add_time', 'edit_time']
    search_fields = ['case_id', 'step_seqnum', 'step_id']
    list_filter = ['case_id', 'step_seqnum', 'step_id']
