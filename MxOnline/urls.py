
from django.contrib import admin
from django.urls import path
import xadmin
from apps.operations.views import IndexView
# from apps.users import views
from django.views.generic import TemplateView
from apps.users.views import LoginView, LogoutView
from apps.organizations.views import OrgView
from django.conf.urls import url,include
from django.views.static import serve
from MxOnline.settings import MEDIA_ROOT
urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    # path('', TemplateView.as_view(template_name='index.html'),name='index'),
    path('courselist/', TemplateView.as_view(template_name='course-list.html'), name='course_list'),
    path('', IndexView.as_view(),name='index'),
    path('login/', LoginView.as_view(),name='login'),
    # 配置授课机构列表展示
    path('orglist/', OrgView.as_view(),name='org_list'),
    path('logout/',LogoutView.as_view(), name ='logout'),
#     配置上传文件的访问url
    url(r'^media/(?P<path>.*)$',serve,{"document_root":MEDIA_ROOT}),
    # 授课机构相关操作
    url(r'^org/', include(('apps.organizations.urls', 'organizations'), namespace='org')),
    # 课程相关页面
    url(r'^course/', include(('apps.courses.urls', 'courses'), namespace='course')),
    # 用户操作相关
    url(r'^op/', include(('apps.operations.urls', 'operations'), namespace='op')),
    url(r'^users/', include(('apps.users.urls', 'users'), namespace='users')),

]
