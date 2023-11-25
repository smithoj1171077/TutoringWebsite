from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('',views.books,name='bookindex'),
    path('<int:pk>/',views.bookdetail,name='bookdetail'),
    path('add/<int:revisionbook_id>/cart',views.add_to_cart,name='add_to_cart'),
    path('remove/<int:item_id>/cart',views.remove_from_cart,name='remove_from_cart'),
    path('store/', views.view_cart, name='view_cart'),
    path('check_out/', views.check_out, name='check_out'),
]