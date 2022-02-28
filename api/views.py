from rest_framework import viewsets

from api.models import Group
from api.serializers import GroupSerializer


# Create your views here.

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
