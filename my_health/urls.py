"""my_health URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar
# from . models 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('user/', include('services.profile.urls')),
    path('appointment/', include('services.appointment_service.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



























# from django.urls import path, include
# from . import views
# from rest_framework.routers import DefaultRouter


# # router = DefaultRouter()
# # router.register('signup', views.SignUpViewSet)
# # router.register('verify/otp', views.VerifyOtpViewSet)
# # router.register('results', views.ElectionResultViewSet, basename='results')

# urlpatterns = [
#     path('signup/', views.SignUpViewSet.as_view()),
#     path('verify/otp/', views.VerifyOtpViewSet.as_view()),
#     # path('login/', views.LoginView.as_view()),
# ]