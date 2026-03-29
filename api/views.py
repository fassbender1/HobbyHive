from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.serializers import GroupSerializer
from groups.models import Group


class GroupListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)