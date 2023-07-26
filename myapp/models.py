from django.db import models

# Create your models here.

# 1.คำสั่งสร้าง migrations 
# python manage.py makemigrations

# 2.คำสั่งอัพตารางเข้าฐานข้อมูล
# python manage.py migrate

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    # Class Meta
    class Meta:
        verbose_name ="ชื่อคน"
        verbose_name_plural="อายุคน"

    # แปลง object เป็น string ในหน้า Admin
    # self.name = เอาชื่อมาแสดงผล
    # str(self.age) นำอายุมาแสดงโดยแปลงเป็น string
    def __str__(self):
        return "ชื่อ " + self.name +", อายุ " + str(self.age)

