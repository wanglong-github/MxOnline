from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from apps.users.views import *

urlpatterns = [
    url(r'^info/$', UserInfoView.as_view(), name='info'),

    # url(r'^mycourse/$', MyCourseView.as_view(), name='mycourse'),
    url(r'^mycourse/$', login_required(TemplateView.as_view(template_name='usercenter-mycourse.html'), login_url = '/login/'), {"current_page": "mycourse" }, name='mycourse'),
    url(r'^myfav-course/$', login_required(TemplateView.as_view(template_name='usercenter-fav-course.html'), login_url = '/login/'), {"current_page": "myfav" }, name='myfav-course'),
    url(r'^myfav-org/$', login_required(TemplateView.as_view(template_name='usercenter-fav-org.html'), login_url = '/login/'), {"current_page": "myfav" }, name='myfav-org'),
    url(r'^myfav-teacher/$', login_required(TemplateView.as_view(template_name='usercenter-fav-teacher.html'), login_url = '/login/'), {"current_page": "myfav" }, name='myfav-teacher'),
    url(r'^message/$', login_required(TemplateView.as_view(template_name='usercenter-message.html'), login_url = '/login/'), {"current_page": "message" }, name='message'),

]