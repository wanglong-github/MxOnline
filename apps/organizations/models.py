from django.db import models

# Create your models here.
from apps.users.models import BaseModel
from apps.users.models import UserProfile
class City(BaseModel):
    name = models.CharField(verbose_name='城市名',max_length=20)
    describe = models.CharField(verbose_name='描述',max_length=50)

    class Meta:
        verbose_name = "城市"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

class CourseOrg(BaseModel):
    city = models.ForeignKey(City,verbose_name="所在城市" ,on_delete=models.CASCADE)
    name = models.CharField(verbose_name='机构名称',max_length=30)
    tag = models.CharField(verbose_name="机构标签",max_length=100)
    category = models.CharField(verbose_name="机构类别",max_length=10,choices=(('gr','个人'),('gx','高校'),('pxjg','培训机构')))
    fav_nums = models.IntegerField(verbose_name='收藏数',default=0)
    image = models.ImageField(verbose_name="logo",upload_to="org/%Y/%m",max_length=100)
    url = models.CharField(verbose_name='机构地址',max_length=300)
    students = models.IntegerField(verbose_name='学习人数',default=0)
    click_nums = models.IntegerField(verbose_name='点击数', default=0)
    class_nums = models.IntegerField(verbose_name='课程数',default=0)
    is_CCC = models.BooleanField(verbose_name="是否认证",default=False)
    is_gold = models.BooleanField(verbose_name="是否金牌",default=False)

    class Meta:
        verbose_name= '机构'
        verbose_name_plural= verbose_name
    def __str__(self):
        return self.name

class Teacher(BaseModel):
    user = models.OneToOneField(UserProfile, verbose_name="用户",on_delete=models.SET_NULL, null=True, blank=True)
    subsidiary_organ = models.CharField(verbose_name='所属机构',max_length=100)
    techaer = models.CharField(verbose_name='教师名',max_length=10)
    working = models.IntegerField(verbose_name='工作年限',default=0)
    company = models.CharField(verbose_name='就职公司',max_length=30,default="")
    position = models.CharField(verbose_name='公司职位',max_length=20,default="")
    style = models.CharField(verbose_name='教学特点',max_length=1000,default="")

    fav_nums = models.IntegerField(verbose_name="收藏数",default=0)
    age = models.IntegerField(verbose_name='年龄',default=0)
    image = models.ImageField(upload_to="teacher/%Y/%m", verbose_name="头像", max_length=100)

    class Meta:
        verbose_name='讲师'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name
