from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('main_app.urls', 'main_app'), namespace='main')),
    path('users/', include(('user.urls', 'user'), namespace='user')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
