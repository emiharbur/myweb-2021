from django.db import models

# Create your models here.
class newstable(models.Model):
    area_list=(
        ('1','美国'),
        ('2','中国'),
        ('3','欧洲'),
        ('4','原油'),
        ('5', '日本'),
        ('6','拉丁美洲'),
        ('7','澳洲'),
        ('8','其他'),
    )

    important_list=(
        ('0','just for fun'),
        ('1','不重要'),
        ('2','一般'),
        ('3','重要'),
        ('4','十分重要'),
        ('9','待定'),
    )

    id = models.CharField(max_length=20,primary_key=True)
    datetime_list = models.DateTimeField(null=True,blank=True)
    news = models.TextField(null=True,blank=True)
    area = models.CharField(max_length=3,choices=area_list,null=True,blank=True)
    important= models.CharField(max_length=1, choices=important_list,null=True,blank=True)
    note=models.CharField(max_length=100,null=True,blank=True)
    isDelete = models.BooleanField(default=False,null=True)
    class Meta:
        db_table='newstable'



