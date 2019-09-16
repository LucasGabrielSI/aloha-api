from django.urls import path
from aloha_app import settings
from django.contrib import admin
from aloha_app.routers import router
from django.conf.urls import include
from django.conf.urls.static import static


admin.site.site_header = 'Aloha'
admin.site.index_title = 'Aloha'
admin.site.site_title = 'Aloha'

urlpatterns = [
    path('', admin.site.urls),
    path('api/', include(router.urls)),
]
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
