from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from groups.models import Group
from events.models import Event
from interactions.models import Comment
from hobbies.models import Hobby

from .serializers import *
from .permissions import IsOwnerOrReadOnly

# class GroupListAPI(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request):
#         groups = Group.objects.all()
#         serializer = GroupSerializer(groups, many=True)
#         return Response(serializer.data)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()

    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [OrderingFilter]

    ordering_fields = ['date', 'title']
    ordering = ['-date']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Event.objects.filter(organizer=self.request.user)
        return Event.objects.all()

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

    @action(detail=True, methods=['get'])
    def participants(self, request, pk=None):
        event = self.get_object()
        return Response({
            "count": event.participants.count()
        })

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class HobbyViewSet(viewsets.ModelViewSet):
    queryset = Hobby.objects.all()
    serializer_class = HobbySerializer