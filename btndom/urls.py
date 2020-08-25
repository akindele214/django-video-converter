"""btndom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework import routers
from converter.converter_viewsets import (AllMediaViewSet, ProcessedMediaViewSet,ProcessingMediaViewSet,
                FailedMediaViewSet, WaitingMediaViewSet, UnavailableMediaViewSet)

router = routers.DefaultRouter()
# router.register(r'documents', DocumentViewSet)
router.register(r'all_doc', AllMediaViewSet)
router.register(r'done_doc', ProcessedMediaViewSet)
router.register(r'failed_doc', FailedMediaViewSet)
router.register(r'queued_doc', WaitingMediaViewSet)
router.register(r'unavailable', UnavailableMediaViewSet)
router.register(r'processing', ProcessingMediaViewSet)


urlpatterns = [
    path('api/v1/', include((router.urls, "api"), namespace="api")),
    path('api/auth/', include('rest_framework.urls')),
    
    path('admin/', admin.site.urls),
    
    path('', include('demo.urls', namespace='demo')),
    path('c/', include('converter.urls', namespace='converter'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
