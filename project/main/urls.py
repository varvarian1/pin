from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='main')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)