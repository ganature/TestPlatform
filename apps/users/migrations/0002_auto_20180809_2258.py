# Generated by Django 2.0.7 on 2018-08-09 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('1', '测试人员'), ('2', '开发人员')], max_length=20, verbose_name='角色'),
        ),
    ]
