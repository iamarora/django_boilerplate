from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from djangoapp.models import DummyModal
from djangoapp.serializers import DummySerializer
from djangoapp.tasks import asyncTask


class DummyViewSet(viewsets.ModelViewSet):
    queryset = DummyModal.objects.all()
    serializer_class = DummySerializer


class AsyncView(APIView):
    def get(self, request):
        asyncTask.delay()
        return Response({"data": []})
