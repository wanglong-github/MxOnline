import xadmin
from apps.organizations.models import CourseOrg
from apps.organizations.models import City
from apps.organizations.models import Teacher

class organizationsAdmin(object):
    pass
xadmin.site.register(CourseOrg,organizationsAdmin)

class CityAdmin(object):
    pass
xadmin.site.register(City,CityAdmin)

class TeacherAdmin(object):
    pass
xadmin.site.register(Teacher,TeacherAdmin)