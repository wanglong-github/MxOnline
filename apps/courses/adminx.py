import xadmin
from apps.courses.models import Course

class CourseAdmin(object):
    pass
xadmin.site.register(Course,CourseAdmin)