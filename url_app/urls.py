from django.urls import path
from .views import HomeView
from django.contrib.auth import views as auth_views
from .views import SignUpView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'), 
]