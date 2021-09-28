from typing import Pattern
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index, name='index'),
    path('index',views.index, name='index'),
    path('gallery',views.gallery, name='gallery'),
    path('faculty',views.faculty, name='faculty'),
    path('fac_Dashboard',views.fac_Dashboard,name='fac_dashboard'),
    path('fac_reg',views.fac_reg, name='fac_reg'),
    path('stu_reg',views.stu_reg, name='stu_reg'),
    path('edit_profile',views.edit_profile, name='edit_profile'),
    path('stu_Dashboard',views.stu_Dashboard, name='stu_Dashboard'),
    path('student',views.student, name='student'),
    path('logout',views.logout, name='logout'),
    path('render_pdf_view',views.render_pdf_view, name='render_pdf_view'),
    path('payment/checkout',views.checkout, name='checkout'),
    path('payment/handlerequest',views.handlerequest, name='handlerequest'),
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),


   
    
    
    
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)