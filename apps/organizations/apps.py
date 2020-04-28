from django.apps import AppConfig


class OrganizationsConfig(AppConfig):
    name = 'apps.organizations'
    verbose_name = '机构管理'

class CityConfig(AppConfig):
    name = 'apps.City'
    verbose_name = '城市管理'

class TeacherConfig(AppConfig):
    name = 'apps.Teacher'
    verbose_name = '讲师管理'
