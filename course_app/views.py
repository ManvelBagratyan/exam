from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, HttpResponseRedirect
from .models import Course, Lecture
from django.contrib.auth import authenticate, login as _login, logout as _logout
from django.contrib.auth.models import User

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_app/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_app/course_detail.html', {'course': course})

def rate_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
         rating = float(request.POST.get('rating'))
         course.add_rating(rating)
         return redirect('course_app:course_detail', course_id=course.id)
    return render(request, 'course_app/rate_course.html', {'course': course})



def register(request):
    if request.method == "GET":
        return render(request, "course_app/register.html", {})
    else:
        try:
            first_name = request.POST["firstname"]
            last_name = request.POST["lastname"]
            email = request.POST["email"]
            age = request.POST["age"]
            password = request.POST["password"]
            repeat_password = request.POST["repeat_password"]
        except:
            return render(request, "course_app/register.html", {"error_message": "Missed Field"})        

        if password != repeat_password:
            return render(request, "course_app/register.html", {"error_message": "Password not match."})        

    user = User.objects.create_user(username=email, email=email, password=password)
    user.first_name=first_name
    user.last_name = last_name
    user.save()
    
    app_user = Lecture(user=user, age=age)
    app_user.save()

    return  HttpResponseRedirect('/course_app/login/')


def login(request):
    if request.method == "GET":
        return render(request, 'course_app/login.html', {})
    else:
        try:
            email = request.POST["email"]
            password = request.POST["password"]
        except:
            return render(request, "course_app/login.html", {"error_message": "Missed Field"}) 
        
    user = authenticate(username=email, password=password)
    print("USER", email, password)
    if user:
        _login(request, user)
        return HttpResponseRedirect('/course_app/')

    else:
        return render(request, "course_app/login.html", {"error_message": "Email or password is incorrect."}) 
    

def logout(request):
    _logout(request)
    return HttpResponseRedirect("/course_app/login")
