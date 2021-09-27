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
        kwargs = {column: value}
        try:
            items = Item.objects.filter(**kwargs)
            return items
        except Item.DoesNotExist:
            raise Http404

    def more(self, column, value):
        column += '__gt'
        kwargs = {column: value}
        try:
            items = Item.objects.filter(**kwargs)
            return items
        except Item.DoesNotExist:
            raise Http404

    def less(self, column, value):
        column += '__lt'
        kwargs = {column: value}
        try:
            items = Item.objects.filter(**kwargs)

            return items
        except Item.DoesNotExist:
            raise Http404

    def contains(self, column, value):
        try:
            items = Item.objects.filter(name__icontains=value)
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