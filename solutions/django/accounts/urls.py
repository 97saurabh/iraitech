from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'accounts'
urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html',redirect_authenticated_user=True),name='login'),
    path('signup/',views.SignUp,name='signup'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]