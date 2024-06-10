from django.urls import path, include
from. import views


urlpatterns = [
    path('',views.createUser,name="createUser"),
    path('update/<int:id>/',views.updateUser,name="updateeUser"),
    path('delete/<int:id>/',views.deleteUser,name="deleteUser"),
    path('getUser/<int:id>/',views.getUser,name="getUser")
]
