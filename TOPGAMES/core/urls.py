from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index, login, carrito, modificar_perfil


urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('carrito/', carrito, name='carrito'),
    path('modificar_perfil/', modificar_perfil, name='modificar_perfil'),
    
    
    #recuperación de contraseña
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='core/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='core/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='core/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='core/password_reset_complete.html'), name='password_reset_complete'),
]
