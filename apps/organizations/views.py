from django.shortcuts import render
from django.views.generic import View
from apps.organizations.models import CourseOrg,City,Teacher
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
class OrgView(View):
    def get(self,request,*args,**kwargs):
        # 展示授课机构列表
        all_orgs=CourseOrg.objects.all()
        all_city=City.objects.all()
        #
        category=request.GET.get('ct','')

        if category:
            all_orgs=all_orgs.filter(category=category)

        #对所在城市筛选
        city_id=request.GET.get('city','')
        if city_id:
            if city_id.isdigit():
                all_orgs=all_orgs.filter(city_id=int(city_id))

        org_nums = all_orgs.count()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs,per_page=10, request=request)#per_pagr每页显示几个
        orgs=p.page(page)

        return render(request,'org-list.html',
                      {'city_id':city_id,'all_orgs':orgs,'all_city':all_city,'org_nums':org_nums,'category':category,})