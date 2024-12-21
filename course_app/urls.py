from django.urls import path
from . import views

app_name = 'course_app'

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('course_app/<int:course_id>/', views.course_detail, name='course_detail'),
    path('course_app/<int:course_id>/rate/', views.rate_course, name='rate_course'),
    path("register/", views.register, name="register"),
    path("login/", views.login, name='login'),
    path("logout", views.logout, name='logout'),
]
