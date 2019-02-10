from django.urls import path
from .views import signup, profile
from django.contrib.auth import views as login_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', login_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
    path('password-reset/',
    	 login_view.PasswordResetView.as_view(template_name='password_reset/password_reset.html'),
	     name='password_reset'
	    ),
    path('password-reset/done', 
    	login_view.PasswordResetDoneView.as_view(template_name='password_reset/password_reset_done.html'),
    	name='password_reset_done'
    	),
    path('password-reset-confirm/<str:uidb64>/<str:token>',
    	login_view.PasswordResetConfirmView.as_view(template_name='password_reset/password_reset_confirm.html'),
    	name='password_reset_confirm'
    	),
    path('password-reset-complete',
    	login_view.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
    	name='password_reset_complete'
    	),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # To display uploaded users images
