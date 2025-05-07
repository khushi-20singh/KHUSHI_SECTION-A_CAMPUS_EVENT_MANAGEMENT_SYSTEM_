from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import (
    EventViewSet,
    NoticeViewSet,
    CertificateViewSet,
    EventListView,
    NoticeListView,
    CertificateListView,
    RegisterAPIView,
    answer_question,
    register_for_event,
)

router = DefaultRouter()

# Admin access endpoints
router.register(r'events', EventViewSet, basename='admin-events')
router.register(r'notices', NoticeViewSet, basename='admin-notices')
router.register(r'certifications', CertificateViewSet, basename='admin-certificates')

# Read-only endpoints for students
router.register(r'events/list', EventListView, basename='event-list')
router.register(r'notices/list', NoticeListView, basename='notice-list')
router.register(r'certifications/list', CertificateListView, basename='certificate-list')

urlpatterns = [
    path('', include(router.urls)),

    # User signup
    path('register/', RegisterAPIView.as_view(), name='register'),

    # Token-based login
    path('login/', obtain_auth_token, name='login'),

    # Chatbot / Q&A (if you need it)
    path('answer/', answer_question, name='answer'),

    # Student event registration
    path('events/register/', register_for_event, name='register-event'),
]
