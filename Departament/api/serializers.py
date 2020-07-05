from rest_framework.serializers import ModelSerializer
from Departament.models import Departament

class DepartamentSerializer(ModelSerializer):
    class Meta:
        model = Departament
        fields = '__all__'
