from django.contrib import admin
from django.urls import path,include

from django.config import settings
from django.config.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', include('personal_information.urls')),
    path('evaluation/', include('evaluation.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
