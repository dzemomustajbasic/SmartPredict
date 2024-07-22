from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('titanic', views.titanic_survival, name='titanicsurvival'),
    path('titanic/results', views.titanic_results, name="titanic-results"),
    path('laptop/', views.laptop_price_prediction, name='laptop'),
    path('laptop-results/', views.laptop_results, name='laptop-results'),
    path('accounts/<str:username>/', views.user_profile, name='user-profile'),
    path('accounts/<str:username>/change-password/', views.change_password, name='change_password'),
    path('dashboard/', views.admin_dashboard, name='admin-dashboard'),
    path('user/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('user/edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('user/create/', views.create_user, name='create_user'),
]
