from django.http import Http404
from .models import Item
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ItemSerializer, DataSerializer


class ItemList(APIView):
    def get_object(self):
        try:
            return Item.objects.all()
        except Item.DoesNotExist:
            raise Http404

    def get(self, request):
        items = self.get_object()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


class Answer(APIView):
    def post(self, request):
        # serializer = DataSerializer(request.data, many=True)
        print(request.data)
        return Response(request.data)
