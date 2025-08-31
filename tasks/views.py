from rest_framework.views import APIView
from rest_framework import status, permissions, generics
from rest_framework.pagination import PageNumberPagination
from .models import Task
from .serializers import TaskSerializer, SerializerRegister
from rest_framework.response import Response


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        #Get user tasks

        queryset = Task.objects.filter(user=self.request.user)

        #Filter

        completed = self.request.query_params.get('completed')
        if completed is not None:
            if completed.lower() == 'true':
                queryset = queryset.filter(is_completed=True)
            if completed.lower() == 'false':
                queryset = queryset.filter(is_completed=False)

        #Ordering
        ordering = self.request.query_params.get('ordering')
        if ordering in ['created_at', '-created_at']:
            queryset = queryset.order_by(ordering)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)



class RegisterView(APIView):

    permission_classes = []

    def post(self, request):
        serializer = SerializerRegister(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User create successfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
