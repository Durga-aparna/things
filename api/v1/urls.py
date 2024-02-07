from django.urls import path
from api.v1 import views
urlpatterns = [
    path("get",views.get_details),
    path("post",views.post_details),
    path("patch",views.Bus_details),
    path("put",views.vehicle_details),
    path("delete",views.edit_details),
    path('Get/<int:V_NUM>',views.dynamic)
]
