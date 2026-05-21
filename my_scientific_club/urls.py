from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Dit koppelt de URLs van onze scientific_app aan de hoofd-URL van de website
    path('', include('scientific_app.urls')),
]