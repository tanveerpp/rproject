from rest_framework import viewsets
from .EmpSerializer import EmpSerializer
from .models import Emp
class EmpViewset(viewsets.ModelViewSet):
    queryset=Emp.objects.all()
    serializer_class=EmpSerializer