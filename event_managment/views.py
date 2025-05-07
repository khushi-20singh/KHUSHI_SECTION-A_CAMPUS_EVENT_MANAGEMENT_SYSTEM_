
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView

from .models import Event, Notice, Certificate, EventRegistration
from .serializers import (
    EventSerializer,
    NoticeSerializer,
    CertificateSerializer,
    RegisterSerializer,
    EventRegistrationSerializer,
)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAdminUser]  # Admin-only CRUD

class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = [IsAdminUser]

class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAdminUser]

# ---------------- Student Read-Only ViewSets ---------------- #

class EventListView(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all().order_by('-date')[:3]
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]  # Students view only

class NoticeListView(viewsets.ReadOnlyModelViewSet):
    queryset = Notice.objects.all().order_by('-published_date')[:3]
    serializer_class = NoticeSerializer
    permission_classes = [IsAuthenticated]

class CertificateListView(viewsets.ReadOnlyModelViewSet):
    queryset = Certificate.objects.all().order_by('-issue_date')[:3]
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticated]

# ---------------- User Registration ---------------- #

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')

    if not username or not password:
        return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(
        username=username,
        password=password,
        email=email,
        first_name=first_name,
        last_name=last_name
    )

    return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)

class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

# ---------------- General Question Answer Endpoint ---------------- #

@api_view(['POST'])
def answer_question(request):
    question = request.data.get('question', '')
    return JsonResponse({'answer': f'You asked: {question}'})


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def register_for_event(request):
    user = request.user
    event_id = request.data.get("event_id")
    if not event_id:
        return Response({"error": "Event ID is required."}, status=400)
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        return Response({"error": "Event not found."}, status=404)

    registration, created = EventRegistration.objects.get_or_create(user=user, event=event)
    if not created:
        return Response({"message": "Already registered."})
    return Response({"message": "Registered successfully."})
