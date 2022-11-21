from django.contrib import admin
from django.urls import path, include
# 이미지
from django.conf.urls.static import static
from django.conf import settings

from . import views


from django.conf.urls.static import static
urlpatterns = [
    path('',views.index),
    path('admin/', admin.site.urls),
    path('share/', include('share.urls')),
    path('common/', include('common.urls'))
]


# 이미지업로드관련
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
