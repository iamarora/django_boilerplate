from djangoapp.models import DummyModal
from rest_framework import serializers


class DummySerializer(serializers.ModelSerializer):
    class Meta:
        model = DummyModal
        fields = '__all__'
