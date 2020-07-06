from rest_framework.viewsets import ModelViewSet
from Departament.models import Departament
from Departament.api.serializers import DepartamentSerializer

class DepartamentViewSet(ModelViewSet):

    queryset = Departament.objects.all()
    serializer_class = DepartamentSerializer
    filter_fields = '__all__'