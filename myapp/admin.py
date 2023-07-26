from django.contrib import admin
from myapp.models import Person

# Register your models here.
# ปรับแต่งหน้า Admin
class DesigeAdmin(admin.ModelAdmin):
    # แสดงผลแบบตาราง
    list_display=["id","name","age"]
    # กำหนดจำนวนแถวที่แสดง
    list_per_page= 10
    # ตัวกรองข้อมูล
    list_filter=["name","age"]
    # ค้นหาข้อมูล
    search_fields=["name"]
    # สลับฟิลด์การป้อนข้อมูล
    # fields = ["age","name"]
    # สามารถแก้ไขข้อมูลได้ในหน้าแรก
    # list_editable=["age"]



admin.site.register(Person,DesigeAdmin)