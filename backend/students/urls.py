
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('student-form/', views.student_form, name='student_form'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_page, name='logout'),
    path('students/', views.student_list, name='student_list'),
    path('products/', views.products, name='products'),
]