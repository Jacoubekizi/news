from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('singup/', views.SingupView.as_view(), name='singup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('list/', views.ListView.as_view(), name='list'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtian_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]