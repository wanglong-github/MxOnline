# Generated by Django 2.2 on 2020-04-28 23:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=20, verbose_name='城市名')),
                ('describe', models.CharField(max_length=50, verbose_name='描述')),
            ],
            options={
                'verbose_name': '城市',
                'verbose_name_plural': '城市',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('subsidiary_organ', models.CharField(max_length=100, verbose_name='所属机构')),
                ('techaer', models.CharField(max_length=10, verbose_name='教师名')),
                ('working', models.IntegerField(default=0, max_length=2, verbose_name='工作年限')),
                ('company', models.CharField(default='', max_length=30, verbose_name='就职公司')),
                ('position', models.CharField(default='', max_length=20, verbose_name='公司职位')),
                ('style', models.CharField(default='', max_length=1000, verbose_name='教学特点')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏数')),
                ('age', models.IntegerField(default=0, verbose_name='年龄')),
                ('image', models.ImageField(upload_to='teacher/%Y/%m', verbose_name='头像')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '讲师',
                'verbose_name_plural': '讲师',
            },
        ),
        migrations.CreateModel(
            name='CourseOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=30, verbose_name='机构名称')),
                ('tag', models.CharField(max_length=100, verbose_name='机构标签')),
                ('category', models.CharField(choices=[('gr', '个人'), ('gx', '高校')], max_length=2, verbose_name='机构类别')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏数')),
                ('image', models.ImageField(upload_to='org/%Y/%m', verbose_name='logo')),
                ('url', models.CharField(max_length=300, verbose_name='机构地址')),
                ('studengts', models.IntegerField(default=0, verbose_name='学习人数')),
                ('class_nums', models.IntegerField(default=0, verbose_name='课程数')),
                ('is_CCC', models.BooleanField(default=False, verbose_name='是否认证')),
                ('is_gold', models.BooleanField(default=False, verbose_name='是否金牌')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.City', verbose_name='所在城市')),
            ],
            options={
                'verbose_name': '机构',
                'verbose_name_plural': '机构',
            },
        ),
    ]
