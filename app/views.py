from django.shortcuts import render
from rest_framework import generics
from .serializers import CompanySerializer, DockSerializer
from .models import Dock, Company
from rest_framework import permissions
from rest_framework.exceptions import APIException

# Create your views here.


class CreateDockView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Dock.objects.all()
    serializer_class = DockSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Dock."""
        serializer.save()


class CreateCompanyView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Company."""
        serializer.save()


class DetailDockView(generics.ListAPIView):
    """This class defines the list behavior of our Campaign entity."""
    serializer_class = DockSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)  # This lets read without authentication
    lookup_url_kwarg = "company_id"

    def get_queryset(self):
        """
        This view should return only quotations from the company_id in the url parameter
        """
        company_id = self.kwargs.get(self.lookup_url_kwarg)
        try:
            company = Company.objects.get(id=company_id)
        except:
            raise APIException("This company does not exists")

        return Dock.objects.filter(initials=company)