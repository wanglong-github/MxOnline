from django.shortcuts import render
from django.views.generic import View
from apps.organizations.models import CourseOrg,City,Teacher
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from apps.organizations.forms import AddAskForm
from django.http import JsonResponse
# Create your views here.
class OrgView(View):
    def get(self,request,*args,**kwargs):
        # 展示授课机构列表
        all_orgs=CourseOrg.objects.all()
        all_city=City.objects.all()
        hot_orgs=all_orgs.order_by('-click_nums')[:3]
        #
        category=request.GET.get('ct','')

        if category:
            all_orgs=all_orgs.filter(category=category)

        #对所在城市筛选
        city_id=request.GET.get('city','')
        if city_id:
            if city_id.isdigit():
                all_orgs=all_orgs.filter(city_id=int(city_id))

        # 对课程机构排序,'-'：倒序排序
        sort = request.GET.get('sort'," ")
        if sort == 'students':
        #     人数排序
            all_orgs=all_orgs.order_by('-students')
        elif sort == 'courses':
            all_orgs=all_orgs.order_by('-class_nums')

        org_nums = all_orgs.count()


        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs,per_page=5, request=request)#per_pagr每页显示几个
        orgs=p.page(page)

        return render(request,'org-list.html',
                      {'city_id':city_id,
                       'all_orgs':orgs,
                       'all_city':all_city,
                       'org_nums':org_nums,
                       'category':category,
                       'sort':sort,
                       'hot_orgs':hot_orgs,
                       })

class AddAsk(View):
    """处理用户咨询模块"""
    def post(self, request, *args, **kwargs):
        userask_form = AddAskForm(request.POST)
        if userask_form.is_valid():
            userask_form.save(commit=True)
            return JsonResponse({
                "status":"success",
                "msg":"提交成功"
            })
        else:
            return JsonResponse({
                "status": "fail",
                "msg": "添加出错"
            })

class TeacherListView(View):
    def get(self, request, *args, **kwargs):
        all_teachers = Teacher.objects.all()
        teacher_nums = all_teachers.count()

        hot_teachers = Teacher.objects.all().order_by("-click_nums")[:3]


        # 讲师分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_teachers,per_page=5, request=request) # 每页显示多少个
        teachers = p.page(page)

        return render(request,'teachers-list.html',{
            "teachers":teachers,
        })
class TeacherDeatailView(View):
    def get(self, request, teacher_id,*args, **kwargs):
        teacher = Teacher.objects.get(id=int(teacher_id))
        return render(request, 'teacher-detail.html', {
            "teacher":teacher
        })