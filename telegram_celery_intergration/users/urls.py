from django.urls import path
from .views import PublicEndpoint, ProtectedEndpoint, LoginView, RegisterView

urlpatterns = [
    path('public/', PublicEndpoint.as_view(), name='public'),
    path('protected/', ProtectedEndpoint.as_view(), name='protected'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
] 