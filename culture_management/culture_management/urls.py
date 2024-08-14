from django.contrib import admin
from django.urls import path, include
from app_culture_management import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', views.signin, name='signin'),
    path('', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='signin'), name='logout'),
    path('', include('app_culture_management.urls')),
]
