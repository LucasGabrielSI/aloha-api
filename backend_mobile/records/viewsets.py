from galery.models import Galery
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from backend_mobile.records.serializers import GalerySerializer


class GaleryViewSet(ModelViewSet):
    queryset = Galery.objects.all()
    serializer_class = [GalerySerializer]
    permission_classes = [AllowAny]

    @action(methods=['GET'], detail=False, permission_classes=[AllowAny])
    def get_all_posts(self, request):
        queryset = Galery.objects.all()
        serializer = GalerySerializer(queryset, many=True)
        return Response(serializer.data)
