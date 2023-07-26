from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Person    # <<Import Class Person มาใช้
from django.contrib import messages # แจ้งเตือนว่าบันทึก

# Create your views here.
# ดึงข้อมูล
def index(request):
    # ดึง Models Person มาใช้ทั้งหมด เก็บไว้ในตัวแปร all_person
    all_person = Person.objects.all()
    # ส่งไปทำงานยัง Index.html   
    return render(request,"index.html",{"all_person":all_person})

#เพิ่มข้อมูล
def about(request):
    if request.method == "POST":
        #รับข้อมูล
        name = request.POST["name"]
        age = request.POST["age"]
        #บันทืกข้อมูล 
        person = Person.objects.create(
            name=name,
            age=age
        )
        person.save()
        messages.success(request,"บันทึกเรียบร้อย")
        #เปลี่ยนเส้นทาง
        return redirect("/")
    else :
        return render(request,"about.html")

#แก้ไขข้อมูล
def edit(request,person_id):
    if request.method == "POST":
        person = Person.objects.get(id=person_id)
        person.name = request.POST["name"]
        person.age = request.POST["age"]
        person.save()
        messages.success(request,"แก้ไขเรียบร้อย")

        return redirect("/")
    else:
        person = Person.objects.get(id=person_id)
        return render(request,"edit.html",{"person":person})
    
# ลบข้อมูล    
def delete(request,person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    messages.success(request,"ลบเรียบร้อย")
    return redirect("/")


