from rest_framework.viewsets import ModelViewSet
from Employees.models import Employee
from .serializers import EmployeesSerializer

class EmployeeViewSet(ModelViewSet):

    queryset = Employee.objects.all()
    serializer_class = EmployeesSerializer
    filter_fields = '__all__'