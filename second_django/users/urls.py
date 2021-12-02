from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_user, name='register'),
    path('edit-profile/', views.edit_user_info, name='edit_profile'),
    path('change-profile/', views.change_user_info, name='change_profile'),
    path('edit/', views.combined_edit, name='combined_edit'),
    path('contact/', views.contact_form, name='contact'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('about-us/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms-and-conditions/', views.terms, name='terms'),
    path('faqs/', views.faqs, name='faqs'),
]
