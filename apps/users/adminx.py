#coding=utf-8
import xadmin
from xadmin import views

from apps.users.models import UserProfile


class UserProfileAdmin(object):
    list_display=('nick_name','role','username')

class BaseSetting(object):
    #添加主题功能
    enable_themes=True
    use_bootswatch=True

class GlobalSettings(object):
    site_title='测试管理平台'
    stie_footer="http://www.cnblogs.com/derek1184405959/"
    #菜单收缩
    menu_style = "accordion"

#xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)