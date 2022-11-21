from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView
from . import views
app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('editinfo/', views.editinfo, name='editinfo'),

    #editpw, changed 추가 (5.28)
    path('editpw/', PasswordChangeView.as_view(template_name = 'common/editpw.html', success_url = '/common/changed'), name='editpw'),
    path('changed/', views.changed, name='changed')
]