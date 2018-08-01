#coding=utf-8
import xadmin

from apps.users.models import UserProfile


class UserProfileAdmin(object):
    list_display=('nick_name','role','username')


#xadmin.site.register(UserProfile,UserProfileAdmin)