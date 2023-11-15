from django.urls import path
from . import views 


"""contains url patterns for the front page"""

app_name = 'frontpage'

urlpatterns = [
    path('', views.frontpage,name='frontpage'),
]

