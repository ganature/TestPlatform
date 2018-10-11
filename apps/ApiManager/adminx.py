import xadmin

from xadmin import views

from apps.ApiManager.models import ProjectInfo,ModuleInfo,ApiInfo,ApiHead,ApiParameter,ApiParameterRaw,ApiResponse

class ProjectInfoAdmin(object):
    list_display = ['project_name', 'responsible_name', 'test_user', 'dev_user','publish_app','simple_desc','other_desc']
    search_fields =['project_name', 'responsible_name', 'test_user', 'dev_user','publish_app','simple_desc','other_desc']
    list_filter = ['project_name', 'responsible_name', 'test_user', 'dev_user','publish_app','simple_desc','other_desc']

class ModuleInfoAdmin(object):
    pass

class ApiInfoAdmin(object):
    pass

class ApiHeadAdmin(object):
    pass


class ApiParameterAdmin(object):
    pass

class ApiParameterRawAdmin(object):
    pass

class ApiResponseAdmin(object):
    pass

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = "测试后台管理系统"
    site_footer = "在线"
    # menu_style = "accordion"

xadmin.site.register(ProjectInfo,ProjectInfoAdmin)
xadmin.site.register(ModuleInfo,ModuleInfoAdmin)
xadmin.site.register(ApiInfo,ApiInfoAdmin)
xadmin.site.register(ApiHead,ApiHeadAdmin)
xadmin.site.register(ApiParameter,ApiParameterAdmin)
xadmin.site.register(ApiParameterRaw,ApiParameterRawAdmin)
xadmin.site.register(ApiResponse,ApiResponseAdmin)
# xadmin.site.register(views.BaseAdminView, BaseSetting)
# xadmin.site.register(views.CommAdminView, GlobalSettings)