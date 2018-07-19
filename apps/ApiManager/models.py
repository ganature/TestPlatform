from django.db import models

# Create your models here.

HTTP_CHOICE = (
    ('HTTP', 'HTTP'),
    ('HTTPS', 'HTTPS')
)

REQUEST_TYPE_CHOICE = (
    ('POST', 'POST'),
    ('GET', 'GET'),
    ('PUT', 'PUT'),
    ('DELETE', 'DELETE')
)

REQUEST_PARAMETER_TYPE_CHOICE = (
    ('form-data', '表单(form-data)'),
    ('raw', '源数据(raw)'),
    ('Restful', 'Restful')
)

PARAMETER_TYPE_CHOICE = (
    ('text', 'text'),
    ('file', 'file')
)

HTTP_CODE_CHOICE = (
    ('200', '200'),
    ('404', '404'),
    ('400', '400'),
    ('502', '502'),
    ('500', '500'),
    ('302', '302'),
)

EXAMINE_TYPE_CHOICE = (
    ('no_check', '不校验'),
    ('only_check_status', '校验http状态'),
    ('json', 'JSON校验'),
    ('entirely_check', '完全校验'),
    ('Regular_check', '正则校验'),
)

UNIT_CHOICE = (
    ('m', '分'),
    ('h', '时'),
    ('d', '天'),
    ('w', '周'),
)

RESULT_CHOICE = (
    ('PASS', '成功'),
    ('FAIL', '失败'),
)


# Create your models here.
class BaseTable (models.Model):
    create_time = models.DateTimeField ('创建时间', auto_now_add=True)
    update_time = models.DateTimeField ('更新时间', auto_now=True)

    class Meta:
        abstract = True
        verbose_name = "公共字段表"
        db_table = 'BaseTable'


class ProjectInfo (BaseTable):
    class Meta:
        verbose_name = '项目信息'
        verbose_name_plural=verbose_name
        db_table = 'ProjectInfo'

    project_name = models.CharField ('项目名称', max_length=50, unique=True, null=False)
    responsible_name = models.CharField ('负责人', max_length=20, null=False)
    test_user = models.CharField ('测试人员', max_length=100, null=False)
    dev_user = models.CharField ('开发人员', max_length=100, null=False)
    publish_app = models.CharField ('发布应用', max_length=100, null=False)
    simple_desc = models.CharField ('简要描述', max_length=100, null=True)
    other_desc = models.CharField ('其他信息', max_length=100, null=True)


class ModuleInfo (BaseTable):
    class Meta:
        verbose_name = '模块信息'
        db_table = 'ModuleInfo'
        verbose_name_plural = verbose_name

    module_name = models.CharField ('模块名称', max_length=50, null=False)
    belong_project = models.ForeignKey (ProjectInfo, on_delete=models.CASCADE)
    test_user = models.CharField ('测试负责人', max_length=50, null=False)
    simple_desc = models.CharField ('简要描述', max_length=100, null=True)
    other_desc = models.CharField ('其他信息', max_length=100, null=True)


class ApiInfo (BaseTable):
    class Meta:
        verbose_name = '接口信息'
        db_table = 'ApiInfo'
        verbose_name_plural = verbose_name

    belong_project = models.ForeignKey (ProjectInfo, on_delete=models.CASCADE)
    belong_module = models.ForeignKey (ModuleInfo, on_delete=models.CASCADE)
    name = models.CharField ('接口名称', max_length=50, null=False)
    httpType = models.CharField ('http/https', max_length=50, default='HTTP', choices=HTTP_CHOICE, null=False)
    requestType = models.CharField ('请求方式', max_length=50, choices=REQUEST_TYPE_CHOICE, null=False)
    apiAddress = models.CharField ('接口地址', max_length=1024, null=False)
    requestParameterType = models.CharField ('请求参数格式', max_length=50, choices=REQUEST_PARAMETER_TYPE_CHOICE, null=False)
    description = models.CharField ('描述', max_length=1024, blank=True, null=True)


class ApiHead (BaseTable):
    class Meta:
        verbose_name = '请求头'
        db_table = 'ApiHead'
        verbose_name_plural = verbose_name

    belong_Api = models.ForeignKey (ApiInfo, on_delete=models.CASCADE)
    name = models.CharField ("标签", max_length=1024, null=False)
    value = models.CharField ("内容", max_length=1024, blank=True, null=True)


class ApiParameter (models.Model):
    class Meta:
        verbose_name = '请求参数'
        db_table = 'ApiParameter'
        verbose_name_plural = verbose_name

    belong_Api = models.ForeignKey (ApiInfo, on_delete=models.CASCADE)
    name = models.CharField ("参数名", max_length=1024)
    type = models.CharField ('参数类型', default="String", max_length=1024, choices=(('Int', 'Int'), ('String', 'String')))
    value = models.CharField ('参数值', max_length=1024, blank=True, null=True)
    required = models.BooleanField ("是否必填", default=True)
    description = models.CharField ("描述", max_length=1024, blank=True, null=True)


class ApiParameterRaw (models.Model):
    class Meta:
        verbose_name = '请求参数Raw'
        db_table = 'ApiParameterRaw'
        verbose_name_plural = verbose_name

    belong_Api = models.ForeignKey (ApiInfo, on_delete=models.CASCADE)
    data = models.TextField ('内容', blank=True, null=True)


class ApiResponse (models.Model):
    class Meta:
        verbose_name = '返回参数'
        db_table = 'ApiResponse'
        verbose_name_plural = verbose_name

    belong_Api = models.ForeignKey (ApiInfo, on_delete=models.CASCADE)
    name = models.CharField ("参数名", max_length=1024, null=False)
    type = models.CharField ('参数类型', default="String", max_length=1024, choices=(('Int', 'Int'), ('String', 'String')))
    value = models.CharField ('参数值', max_length=1024, blank=True, null=True)
    required = models.BooleanField ("是否必填", default=True)
    description = models.CharField ("描述", max_length=1024, blank=True, null=True)
    # 测试




