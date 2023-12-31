"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from student_registration import views

urlpatterns = [
    path("student_registration/insert/", views.insert, name="insert"),
    path("student_registration/student_list/", views.student_list, name="student_list"),
    path(
        "student_registration/match_burmese_data",
        views.match_burmese_data,
        name="match_burmese_data",
    ),
    path(
        "student_registration/matched_second_year_civil",
        views.match_burmese_data_second_year,
        name="matched_second_year",
    ),
    path(
        "student_registration/matched_fourth_year",
        views.match_burmese_data_fourth_year,
        name="matched_fourth_year",
    ),
    path(
        "student_registration/matched_fifth_year",
        views.match_burmese_data_fifth_year,
        name="matched_fifth_year",
    ),
    path(
        "student_registration/matched_sixth_year",
        views.match_burmese_data_sixth_year,
        name="matched_sixth_year",
    ),
    path(
        "student_registration/delete_document/<int:student_id>",
        views.delete_document,
        name="delete_document",
    ),
    path(
        "student_registration/update_document/<int:student_id>",
        views.update_document,
        name="update_document",
    ),
    path(
        "student_registration/second_year",
        views.add_student_second_year,
        name="second_year",
    ),
    path(
        "student_registration/third_year",
        views.add_student_third_year,
        name="third_year",
    ),
    path(
        "student_registration/fourth_year",
        views.add_student_fourth_year,
        name="fourth_year",
    ),
    path(
        "student_registration/fifth_year",
        views.add_student_fifth_year,
        name="fourth_year",
    ),
    path(
        "student_registration/final_year",
        views.add_student_final_year,
        name="final_year",
    ),
    path(
        "student_registration/first_civil",
        views.add_student_first_civil_admin,
        name="first_civil",
    ),
    path(
        "student_registration/first_year",
        views.add_student_first_year,
        name="first_year",
    ),
    path(
        "student_registration/photo_upload_view",
        views.photo_upload_view,
        name="photo_upload_view",
    ),
    path(
        "student_registration/search_by_myanname",
        views.search_by_myanname,
        name="search_by_myanname",
    ),
    path("student_registration/register", views.register, name="register"),
    path("student_registration/signup", views.signup, name="signup"),
    path("student_registration/login", views.login, name="login"),
    path(
        "student_registration/update_student/<str:student_id>",
        views.update_student_admin_second_year,
        name="update_student",
    ),
    path(
        "student_registration/first_civil_list",
        views.student_list_first_civil,
        name="first_civil_list",
    ),

    path(
        "student_registration/new_student_list",
        views.new_student_list,
        name="new_student_list",
    ),
    

    path(
        "student_registration/third_civil_list",
        views.student_list_third_civil,
        name="third_civil_list",
    ),
    path(
        "student_registration/fourth_civil_list",
        views.student_list_fourth_civil,
        name="fourth_civil_list",
    ),
    path(
        "student_registration/fifth_civil_list",
        views.student_list_fifth_civil,
        name="fifth_civil_list",
    ),
    path(
        "student_registration/sixth_civil_list",
        views.student_list_sixth_civil,
        name="sixth_civil_list",
    ),
    path("admin/", admin.site.urls),
]
