
from django.contrib import admin
from django.urls import path
import xadmin
# from apps.users import views
from django.views.generic import TemplateView
from apps.users.views import LoginView
from apps.organizations.views import OrgView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'),name='index'),
    path('login/', LoginView.as_view(),name='login'),
    # 配置授课机构列表展示
    path('orglist/', OrgView.as_view(),name='org_list'),


]
