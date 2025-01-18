from rest_framework import mixins, viewsets

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer