from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API routes handled by event_management app
    path('api/', include('event_management.urls')),

    # Redirect root to API homepage or documentation route
    path('', lambda request: redirect('/api/')),
]
