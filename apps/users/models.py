from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

user_role=(
    (1,u'测试人员'),
    (2,u'开发人员')
)


class UserProfile(AbstractUser):
    nick_name=models.CharField(max_length=50,verbose_name=u'昵称')
    role=models.CharField(choices=user_role,max_length=20,verbose_name=u'角色')
    image = models.ImageField (upload_to="image/%Y/%m", default=u"image/default.png", max_length=100)


    class Meta:
        verbose_name=u'用户信息'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.username

