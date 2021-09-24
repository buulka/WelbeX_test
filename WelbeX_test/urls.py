from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from application import views
# from vue_app.views import ItemTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', views.ItemList.as_view()),
    path('filter/', views.FilteredItems.as_view()),
    path('sort/', views.SortedItems.as_view())
]
