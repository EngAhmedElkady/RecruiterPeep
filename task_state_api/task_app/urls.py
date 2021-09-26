from django.urls import path,include
from . import views
# from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'api/Data', views.SnippetViewSet)
urlpatterns = [
    path('api/data/', views.Data_list), 
    path('api/data/<int:pk>', views.Data_detail,name="data_details"),

    # path('', include(router.urls)),

]
