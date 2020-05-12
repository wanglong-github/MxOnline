from django.conf.urls import url, include
from apps.organizations.views import OrgView,Addask
urlpatterns = [
    url(r'^list/', OrgView.as_view(), name='list'),
    url(r'^add_ask/$', Addask.as_view(), name='add_ask'),

]