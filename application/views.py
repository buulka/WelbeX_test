from django.http import Http404
from .models import Item
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ItemSerializer


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
                items = Item.objects.filter(date__gt=value)
            elif column == 'name':
                items = Item.objects.filter(name__gt=value)
            elif column == 'count':
                items = Item.objects.filter(count__gt=value)
            elif column == 'distance':
                items = Item.objects.filter(distance__gt=value)

            return items
        except Item.DoesNotExist:
            raise Http404

    def less(self, column, value):
        items = []
        try:
            if column == 'date':
                items = Item.objects.filter(date__lt=value)
            elif column == 'name':
                items = Item.objects.filter(name__lt=value)
            elif column == 'count':
                items = Item.objects.filter(count__lt=value)
            elif column == 'distance':
                items = Item.objects.filter(distance__lt=value)

            return items
        except Item.DoesNotExist:
            raise Http404

    def contains(self, column, value):
        try:
            items = Item.objects.filter(name__icontains=value)
            print(items)
            return items
        except Item.DoesNotExist:
            raise Http404

    def post(self, request):
        data = []

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

        serializer = ItemSerializer(data, many=True)

        return Response(serializer.data)


class SortedItems(APIView):

    def sort(self, column):
        try:
            return Item.objects.order_by(column)
        except Item.DoesNotExist:
            raise Http404

    def post(self, request):
        column = request.data['selected_column']
        serializer = ItemSerializer(self.sort(column), many=True)

        return Response(serializer.data)