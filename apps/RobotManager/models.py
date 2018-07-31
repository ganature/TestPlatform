#coding=utf-8
from django.db import models

from apps.users.models import UserProfile
# Create your models here.

class Project(models.Model):
    project_type=(
        (1,'Web自动化'),
        (2,'App自动化'),
        (3,'接口自动化')
    )
    name=models.CharField(max_length=18,verbose_name=u'项目名称')
    type=models.CharField(max_length=20,choices=project_type,verbose_name=u'项目类型')
    creator=models.ForeignKey(UserProfile,verbose_name=u'创建人')
    detail=models.CharField(max_length=50,verbose_name=u'项目描述')
    remark=models.TextField(max_length=200,verbose_name=u'备注')
    add_time=models.DateField(add_time=True,verbose_name=u'创建时间')
    edit_time=models.DateField(auto_now_add=True,verbose_name=u'修改时间')

    class Meta:
        verbose_name=u'测试项目'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name


class Module(models.Model):
    name = models.CharField(max_length=18,verbose_name=u'模块名称')
    belong_project = models.CharField(choices=Project,max_length=20,verbose_name=u'所属项目')
    creator = models.ForeignKey(UserProfile,verbose_name=u'创建人',on_delete=models.SET_NULL,null=True,blank=True)
    detail = models.CharField(max_length=50,verbose_name=u'模块描述')
    remark = models.TextField(max_length=200,verbose_name=u'备注',blank=True,null=True)
    add_time = models.DateField(add_time=True,verbose_name=u'创建时间')
    edit_time = models.DateField(auto_now_add=True,verbose_name=u'修改时间')

    class Meta:
        verbose_name = u'测试模块'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Suites(models.Model):

    suite_num = models.CharField(max_length=20,verbose_name=u'测试集编号')
    name = models.CharField(max_length=18,verbose_name=u'测试集名称')
    belong_module = models.ForeignKey(Module,verbose_name=u'所属模块')
    creator = models.ForeignKey(UserProfile,verbose_name=u'创建人',on_delete=models.SET_NULL,null=True,blank=True)
    detail = models.CharField(max_length=50,verbose_name=u'测试集描述')
    remark = models.TextField(max_length=200,verbose_name=u'备注',blank=True)
    add_time = models.DateField(add_time=True,verbose_name=u'创建时间')
    edit_time = models.DateField(auto_now_add=True,verbose_name=u'修改时间')

    class Meta:
        verbose_name = u'测试集'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Cases(models.Model):
    case_type=(
        (1,'Web自动化'),
        (2,'App自动化'),
        (3,'接口自动化')
    )
    case_status=(
        (1,'未执行'),
        (2,'通过'),
        (3,'失败')
    )
    case_level=(
        ('low','低'),
        ('medium','中'),
        ('high','高')
    )
    case_num=models.CharField(max_length=20,verbose_name=u'用例编号')
    name = models.CharField(max_length=18,verbose_name=u'用例标题')
    type=models.CharField(max_length=20,choices=case_type,verbose_name=u'用例类型')
    belong_project = models.CharField(choices=Project,max_length=20,verbose_name=u'所属项目')
    suite=models.ManyToManyField(Suites,verbose_name=u'测试集')
    expect=models.CharField(max_length=50,verbose_name=u'期望结果')
    status=models.CharField(max_length=20, choices=case_status,verbose_name=u'结果')
    level=models.CharField(max_length=20,choices=case_level,verbose_name=u'用例级别')
    creator = models.ForeignKey(UserProfile,verbose_name=u'创建人',on_delete=models.SET_NULL,null=True,blank=True)
    detail = models.CharField(max_length=50,verbose_name=u'模块描述')
    remark = models.TextField(max_length=200,verbose_name=u'备注',blank=True)
    add_time = models.DateField(add_time=True,verbose_name=u'创建时间')
    edit_time = models.DateField(auto_now_add=True,verbose_name=u'修改时间')

    class Meta:
        verbose_name = u'用例库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Steps(models.Model):
    step_num = models.IntegerField(max_length=20,verbose_name=u'步骤顺序号')
    name = models.CharField(max_length=18,verbose_name=u'测试集名称')
    belong_module = models.ForeignKey(Module,verbose_name=u'所属模块')
    creator = models.ForeignKey(UserProfile,verbose_name=u'创建人',on_delete=models.SET_NULL,null=True,blank=True)
    detail = models.CharField(max_length=50,verbose_name=u'测试集描述')
    remark = models.TextField(max_length=200,verbose_name=u'备注',blank=True)
    add_time = models.DateField(add_time=True,verbose_name=u'创建时间')
    edit_time = models.DateField(auto_now_add=True,verbose_name=u'修改时间')

    class Meta:
        verbose_name = u'操作步骤库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class cases_step(models.Model):
    case_id=models.ForeignKey(Cases,verbose_name=u'测试用例',on_delete=models.SET_NULL,null=True,blank=True)
    step_seqnum=models.IntegerField(default=1,verbose_name=u'操作步骤顺序号')
    step_id=models.ForeignKey(Steps,verbose_name=u'操作步骤',on_delete=models.SET_NULL,null=True,blank=True)

    class Meta:
        verbose_name = u'用例操作步骤'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.case_id