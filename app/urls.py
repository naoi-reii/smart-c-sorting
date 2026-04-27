from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('logs/', views.logs, name='logs'),
    path('settings/', views.settings_view, name='settings'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Settings endpoints
    path('settings/update-username/', views.update_username, name='update_username'),
    path('settings/update-email/', views.update_email, name='update_email'),
    path('settings/update-password/', views.update_password, name='update_password'),
    path('settings/upload-image/', views.upload_image, name='upload_image'),
    path('settings/remove-image/', views.remove_image, name='remove_image'),
]
