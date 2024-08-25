from .serializers import *
from rest_framework import generics, status
from django.utils.translation import gettext as _
from .models import *
from rest_framework.response import Response
from rest_framework import permissions

class ResumeListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    
class ApplicationCreateView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()
    # permission_classes = [IsCareGiver,]

    def post(self, request, *args, **kwargs):
        s = self.serializer_class(data=request.data)
        s.is_valid(raise_exception=True)
        #with transaction.atomic():
        valid = s.validated_data
        resume = Resume.objects.create(first_name = valid.get('first_name')
                                     ,last_name = valid.get('first_name')
                                     ,phone_number = valid.get('phone_number')
                                     ,education = valid.get('education')
                                     ,email = valid.get('email')
                                     ,cv = valid.get('cv')
                                     )
        resume.save()

        return Response({'detail': _("Post created.")}, status=status.HTTP_200_OK)

