from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),

    path('api/booking/', include('apps.booking.api.urls')),
    path('api/clinic/', include('apps.clinic.api.urls')),
    path('api/faq/', include('apps.faq.api.urls')),
    path('api/blog/', include('apps.blog.api.urls')),
    path('api/services/', include('apps.services.api.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
