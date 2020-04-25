from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from dentist import settings

url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.STATIC_ROOT}),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dento.urls')),
]
