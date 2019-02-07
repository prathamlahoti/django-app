from django.urls import path
from .views import signup, profile
from django.contrib.auth import views as login_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', login_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', profile, name='profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # To display uploaded users images
