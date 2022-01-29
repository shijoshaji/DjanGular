from django.urls import path,re_path


from . import views

urlpatterns = [
    re_path(r'^department/$',views.department_api),
    re_path(r'^department/([0-9]+)$',views.department_api),
    re_path(r'^employee/$',views.employee_api),
    re_path(r'^employee/([0-9]+)$',views.employee_api),
]