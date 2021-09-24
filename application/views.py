from django.http import Http404
from .models import Item
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ItemSerializer

data = []

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


class FilteredItems(APIView):


    def equals(self, column, value):
        items = []
        try:
            if column == 'date':
                items = Item.objects.filter(date=value)
            elif column == 'name':
                items = Item.objects.filter(name=value)
            elif column == 'count':
                items = Item.objects.filter(count=int(value))
            elif column == 'distance':
                items = Item.objects.filter(distance=int(value))

            return items
        except Item.DoesNotExist:
            raise Http404

    def more(self, column, value):
        items = []
        try:
            if column == 'date':
                items = Item.objects.raw('SELECT * FROM welbex WHERE date > %s', [value])
            elif column == 'name':
                items = Item.objects.raw('SELECT * FROM welbex WHERE name > %s', [value])
            elif column == 'count':
                items = Item.objects.raw('SELECT * FROM welbex WHERE count > %s', [int(value)])
            elif column == 'distance':
                items = Item.objects.raw('SELECT * FROM welbex WHERE distance > %s', [int(value)])

            return items
        except Item.DoesNotExist:
            raise Http404

    def less(self, column, value):
        items = []
        try:
            if column == 'date':
                items = Item.objects.raw('SELECT * FROM welbex WHERE date < %s', [value])
            elif column == 'name':
                items = Item.objects.raw('SELECT * FROM welbex WHERE name < %s', [value])
            elif column == 'count':
                items = Item.objects.raw('SELECT * FROM welbex WHERE count < %s', [int(value)])
            elif column == 'distance':
                items = Item.objects.raw('SELECT * FROM welbex WHERE distance < %s', [int(value)])

            return items
        except Item.DoesNotExist:
            raise Http404

    def contains(self, column, value):
        try:
            items = Item.objects.raw('SELECT * FROM welbex WHERE name ~ %s', [value])
            return items
        except Item.DoesNotExist:
            raise Http404

    def post(self, request):
        global data

        clause = request.data['selected_clause']
        column = request.data['selected_column']
        value = request.data['sort_value']

        if clause == 'equals':
            data = self.equals(column, value)
        elif clause == 'more':
            data = self.more(column, value)
        elif clause == 'less':
            data = self.less(column, value)
        elif clause == 'contains':
            data = self.contains(column, value)

        return Response()

    def get(self, request):
        global data
        serializer = ItemSerializer(data, many=True)

        return Response(serializer.data)


class SortedItems(APIView):
    def sort(self, column):
        items = []
        try:
            if column == 'name':
                items = Item.objects.raw('SELECT * FROM welbex ORDER BY name')
            elif column == 'count':
                items = Item.objects.raw('SELECT * FROM welbex ORDER BY count')
            elif column == 'distance':
                items = Item.objects.raw('SELECT * FROM welbex ORDER BY distance')
            return items
        except Item.DoesNotExist:
            raise Http404

    def post(self, request):
        global data

        column = request.data['selected_column']
        data = self.sort(column)
        return Response()

    def get(self, request):
        global data
        serializer = ItemSerializer(data, many=True)
        return Response(serializer.data)