from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # O APP SE TORNA A TELA INICIAL
    path('', include('project_app.urls')),

    path('users/', include('users.urls')),
]
