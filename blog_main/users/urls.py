from django.urls import path
from .views import signup
from django.contrib.auth import views as login_view


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', login_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
]