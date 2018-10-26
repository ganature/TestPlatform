# coding=utf-8
from django.db import models

from apps.users.models import UserProfile


# Create your models here.

class Project(models.Model):
    """
    项目模型
    """
    project_type = (
        ('web','Web自动化'),
        ('app','App自动化'),
        ('inface','接口自动化')
    )
    name = models.CharField(max_length=18,verbose_name=u'项目名称',unique=True)
    type = models.CharField(max_length=20,choices=project_type,verbose_name=u'项目类型')
    creator = models.ForeignKey(UserProfile,verbose_name=u'创建人',on_delete=models.SET_NULL,null=True,blank=True)
    detail = models.CharField(max_length=50,verbose_name=u'项目描述')
    remark = models.TextField(max_length=200,blank=True,null=True,verbose_name=u'备注')
    add_time = models.DateField(auto_now_add=True,verbose_name=u'创建时间')
    edit_time = models.DateField(auto_now=True,verbose_name=u'修改时间')

    class Meta:
        verbose_name = u'测试项目'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Module(models.Model):
    """
    模块/包模型
    """
    name = models.CharField(max_length=18,verbose_name=u'模块名称')
    belong_project = models.ForeignKey(Project,verbose_name=u'所属项目',on_delete=models.SET_NULL,null=True,blank=True)
    creator = models.ForeignKey(UserProfile,verbose_name=u'创建人',on_delete=models.SET_NULL,null=True,blank=True)
    detail = models.CharField(max_length=50,verbose_name=u'模块描述')
    remark = models.TextField(max_length=200,verbose_name=u'备注',blank=True,null=True)
    add_time = models.DateField(auto_now_add=True,verbose_name=u'创建时间')
    edit_time = models.DateField(auto_now=True,verbose_name=u'修改时间')

    class Meta:
        verbose_name = u'测试模块'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_belong_project(self,id):
        module=Module.objects.get(id=id)
        project=Project.objects.get()

class Suites(models.Model):
    """
    测试集模型
    """
    suite_num = models.CharField(max_length=20,verbose_name=u'测试集编号')
    name = models.CharField(max_length=18,verbose_name=u'测试集名称')
    belong_module = models.ForeignKey(Module,verbose_name=u'所属模块',on_delete=models.SET_NULL,null=True,blank=True)
    creator = models.ForeignKey(UserProfile,verbose_name=u'创建人',on_delete=models.SET_NULL,null=True,blank=True)
    detail = models.CharField(max_length=50,verbose_name=u'测试集描述')
    remark = models.TextField(max_length=200,verbose_name=u'备注',blank=True)
    add_time = models.DateField(auto_now_add=True,verbose_name=u'创建时间')
    edit_time = models.DateField(auto_now=True,verbose_name=u'修改时间')

    class Meta:
        verbose_name = u'测试集'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Cases(models.Model):
    """
    测试用例模型
    """
    case_type = (
        ('web','Web自动化'),
        ('app','App自动化'),
        ('inface','接口自动化'),
    )
    case_status = (
        ('idle','未执行'),
        ('success','通过'),
        ('fail','失败'),
    )
    case_level = (
        ('low','低'),
        ('medium','中'),
        ('high','高'),
    )
    case_num = models.CharField(max_length=20,verbose_name=u'用例编号')
    name = models.CharField(max_length=18,verbose_name=u'用例标题')
    type = models.CharField(max_length=20,choices=case_type,verbose_name=u'用例类型')
    suite = models.ManyToManyField(Suites,verbose_name=u'测试集')
    expect = models.CharField(max_length=50,verbose_name=u'期望结果')
    status = models.CharField(max_length=20,choices=case_status,verbose_name=u'结果')
    level = models.CharField(max_length=20,choices=case_level,verbose_name=u'用例级别')
    creator = models.ForeignKey(UserProfile,verbose_name=u'创建人',on_delete=models.SET_NULL,null=True,blank=True)
    detail = models.CharField(max_length=50,verbose_name=u'用例描述')
    remark = models.TextField(max_length=200,verbose_name=u'备注',blank=True)
    add_time = models.DateField(auto_now_add=True,verbose_name=u'创建时间')
    edit_time = models.DateField(auto_now=True,verbose_name=u'修改时间')

    class Meta:
        verbose_name = u'用例库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Library(models.Model):
    name = models.CharField(max_length=50,verbose_name=u'Library名称',unique=True)
    doc = models.CharField(max_length=50,verbose_name=u'Library名描述')
    add_time = models.DateField(auto_now_add=True,verbose_name=u'创建时间')
    edit_time = models.DateField(auto_now=True,verbose_name=u'修改时间')

    class Meta:
        verbose_name = u'公用测试库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Keyword(models.Model):
    """
    关键字模型
    """
    name = models.CharField(max_length=50,verbose_name=u'关键字名称')
    doc = models.CharField(max_length=50,verbose_name=u'关键字描述')
    library = models.ForeignKey(Library,verbose_name=u'所属Library',on_delete=models.SET_NULL,null=True,blank=True)
    add_time = models.DateField(auto_now_add=True,verbose_name=u'创建时间')
    edit_time = models.DateField(auto_now=True,verbose_name=u'修改时间')

    class Meta:
        verbose_name = u'关键字库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Resource(models.Model):
    """
    关键字资源
    """
    name = models.CharField(max_length=50,verbose_name=u'Resource名称')
    doc = models.CharField(max_length=100,verbose_name=u'Resource描述')
    module = models.ForeignKey(Module,verbose_name=u'所属模块',on_delete=models.SET_NULL,null=True,blank=True)
    add_time = models.DateField(auto_now_add=True,verbose_name=u'创建时间')
    edit_time = models.DateField(auto_now=True,verbose_name=u'修改时间')

    class Meta:
        verbose_name = u'Resource库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UserKeywords(models.Model):
    name = models.CharField(max_length=50,verbose_name=u'用户关键字名称')
    doc = models.CharField(max_length=100,verbose_name=u'用户关键字描述')
    resource = models.ForeignKey(Resource,on_delete=models.SET_NULL,null=True,blank=True,verbose_name=u'所属Resource')
    keyword = models.ForeignKey(Keyword,on_delete=models.SET_NULL,null=True,blank=True)
    relate_user_keyword = models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True,
                                            verbose_name=u'关联用户关键字')
    add_time = models.DateField(auto_now_add=True,verbose_name=u'创建时间')
    edit_time = models.DateField(auto_now=True,verbose_name=u'修改时间')

    class Meta:
        verbose_name = u'用户关键字库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Steps(models.Model):
    """
    测试步骤模型
    """
    step_num = models.IntegerField(verbose_name=u'步骤顺序号')
    name = models.CharField(max_length=18,verbose_name=u'操作步骤名称')
    keyword = models.ForeignKey(UserKeywords,on_delete=models.SET_NULL,null=True,blank=True)
    creator = models.ForeignKey(UserProfile,verbose_name=u'创建人',on_delete=models.SET_NULL,null=True,blank=True)
    doc = models.CharField(max_length=50,verbose_name=u'操作步骤描述',null=True,blank=True)
    remark = models.TextField(max_length=200,verbose_name=u'备注',blank=True)
    add_time = models.DateField(auto_now_add=True,verbose_name=u'创建时间')
    edit_time = models.DateField(auto_now=True,verbose_name=u'修改时间')

    class Meta:
        verbose_name = u'操作步骤库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CasesStep(models.Model):
    """
    用例和步骤的关系
    """
    case_id = models.ForeignKey(Cases,verbose_name=u'测试用例',on_delete=models.SET_NULL,null=True,blank=True)
    step_seqnum = models.IntegerField(default=1,verbose_name=u'操作步骤顺序号')
    step_id = models.ForeignKey(Steps,verbose_name=u'操作步骤',on_delete=models.SET_NULL,null=True,blank=True)
    add_time = models.DateField(auto_now_add=True,verbose_name=u'创建时间')
    edit_time = models.DateField(auto_now=True,verbose_name=u'修改时间')

    class Meta:
        verbose_name = u'用例操作步骤'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.case_id
