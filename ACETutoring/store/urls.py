from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('',views.books,name='bookindex'),
    path('<int:pk>/',views.bookdetail,name='bookdetail')
]