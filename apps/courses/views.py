from django.shortcuts import render
from django.views.generic.base import View
from apps.courses.models import Course
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
class CourseListView(View):
    def get(self, request, *args, **kwargs):
        # 获取课程列表信息
        all_courses = Course.objects.order_by("-add_time")
        ## 获取热门课程 前3个
        hot_courses = Course.objects.order_by('-click_nums')[:3]
        sort = request.GET.get('sort', "")
        if sort == 'students ':
            # 根据参与人数排序  减号代表倒序排序的意思
            # li><a href="?sort=students">参与人数</a></li>
            all_courses = all_courses.order_by('-students ')
        elif sort == 'hot':
            # 课程排序  <li><a href="?sort=hot">最热门</a></li>
            # 根据最热门进行排序 参与人数  <
            all_courses = all_courses.order_by('-click_nums')
        # 对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses, per_page=6, request=request)  # 每页显示多少个
        courses = p.page(page)

        return render(request, 'course-list.html',
                      {"all_courses": courses,
                       "sort": sort,
                       "hot_courses": hot_courses,

                       })

class CourseDetailView(View):
    def get(self,request,course_id,*args,**kwargs):
        course=Course.objects.get(id=int(course_id))
        # 点击到课程的详情就记录一次点击数
        course.click_nums+=1
        course.save()

        return render(request, 'course-detail.html',
                      {"course":course,

                       },
                    )