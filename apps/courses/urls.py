from django.conf.urls import url, include
from apps.organizations.views import OrgView,AddAsk
from apps.courses.views import CourseListView
urlpatterns = [
    url(r'^list/',CourseListView.as_view(), name='list'),


]