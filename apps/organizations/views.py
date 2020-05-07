from django.shortcuts import render
from django.views.generic import View
# Create your views here.
class OrgView(View):
    def get(self,request,*args,**kwargs):
        # 展示授课机构列表
        return render(request,'org-list.html')