from rest_framework.viewsets import ModelViewSet
from Company.models import Company
from Company.api.serializers import CompanySerializer

class CompanyViewSet(ModelViewSet):
    
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_fields = '__all__'