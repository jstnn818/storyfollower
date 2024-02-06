from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('register_user', views.register_user, name="register"),
    path('access_denied/<owner_name>', views.access_denied, name="access-denied"),
]