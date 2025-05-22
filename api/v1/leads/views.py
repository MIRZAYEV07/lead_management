from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.mail import send_mail
from django.conf import settings
from apps.leads.models import Lead
from apps.user.models import User
from .serializers import LeadSerializer, LeadUpdateSerializer

class LeadCreateView(generics.CreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        lead = serializer.save()

        # Send email to the prospect
        send_mail(
            subject="Thanks for submitting your resume!",
            message=f"Dear {lead.first_name},\n\nWe received your application.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[lead.email],
        )

        # Fetch all attorneys (users) and email them
        attorney_emails = User.objects.values_list('email', flat=True).exclude(email__isnull=True).exclude(email='')

        if attorney_emails:
            send_mail(
                subject="New Lead Submitted",
                message=f"Lead submitted:\n{lead.first_name} {lead.last_name}\n{lead.email}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=list(attorney_emails),
                fail_silently=False,
            )

class LeadListView(generics.ListAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [permissions.IsAuthenticated]

class LeadDetailView(generics.RetrieveAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [permissions.IsAuthenticated]

class LeadUpdateView(generics.UpdateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
