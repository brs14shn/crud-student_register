
from django.urls import path
from .views import student_list,student_add,student_update,student_delete


urlpatterns = [
    path("list/",student_list,name="list"),
    path("",student_add,name="add"),
    path("<int:id>",student_update,name="update"),
    path("delete/<int:id>",student_delete,name="delete")

]