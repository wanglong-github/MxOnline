# Generated by Django 2.2 on 2020-05-11 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='category',
            field=models.CharField(choices=[('gr', '个人'), ('gx', '高校'), ('pxjg', '培训机构')], max_length=10, verbose_name='机构类别'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='working',
            field=models.IntegerField(default=0, verbose_name='工作年限'),
        ),
    ]