from rest_framework.serializers import ModelSerializer
from galery.models import Galery


class GalerySerializer(ModelSerializer):
    class Meta:
        model = Galery
        depth = 1
        fields = '__all__'
