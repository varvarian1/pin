from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'pin-create-tool'

urlpatterns = [
    path('', views.index, name='pin-create-tool')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)