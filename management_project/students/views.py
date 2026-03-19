
from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import STUDENT

def menu(request):
    return render(request, 'menu.html')

def add_students(request):
    if request.method == "POST":
        st_name = request.POST['name']
        st_email = request.POST['email']
        st_age = request.POST['age']

        if st_name == '' or st_email == '' or st_age == '':
            return HttpResponse("all fields should be filled --- ")
        try:
            STUDENT.objects.create(student_name=st_name, student_email=st_email, student_age=st_age)
            return redirect('view_students')
        except Exception as e:
            return HttpResponse(f"Error:{e}")

    return render(request, 'add_students.html')

def update_students(request,id):
    new_val=STUDENT.objects.get(student_id=id)
    if request.method == "POST":
        new_val.student_name=request.POST['new_name']
        new_val.student_email=request.POST['new_email']
        new_val.student_age=request.POST['new_age']

        new_val.save()
        return redirect('menu')
    return render(request, 'update_students.html',{'new_val':new_val})

def delete_students(request,id):
    s_delete=STUDENT.objects.get(student_id=id)
    if request.method == "POST":
        s_delete.delete()
        return redirect('view_students')
    return render(request, 'delete_students.html', {'delete_student': s_delete})


def view_students(request):
    try:
        data=STUDENT.objects.all()
    except Exception as e:
        return HttpResponse("f{error}:{e}")
    return render(request, 'view_students.html',{'students':data})








