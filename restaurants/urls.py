from django.urls import path
from restaurants import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('nutritional_informations', views.NutritionalTypeList.as_view(), name='nutritional_information_list'),
    path('nutritional_informations/view/<int:pk>', views.NutritionalTypeView.as_view(), name='nutritional_view'),
    path('nutritional_informations/new', views.NutritionalTypeCreate.as_view(), name='nutritional_new'),
    path('nutritional_informations/edit/<int:pk>', views.NutritionalTypeUpdate.as_view(), name='nutritional_edit'),
    path('nutritional_informations/delete/<int:pk>', views.NutritionalTypeDelete.as_view(), name='nutritional_delete'),
    path('products', views.product_list, name='product_list'),
    path('products/view/<int:pk>', views.product_view, name='product_view'),
    path('products/new', views.product_create, name='product_new'),
    path('products/edit/<int:pk>', views.product_update, name='product_edit'),
    path('products/delete/<int:pk>', views.product_delete, name='product_delete'),
    path('nutritional_values/new/<int:pId>', views.nutritional_values_create, name='nutritional_values_new'),
    path('nutritiona_values/edit/<int:pk>', views.nutritional_values_update, name='nutritional_values_edit'),
    path('nutritional_values/delete/<int:pk>', views.nutritional_values_delete, name='nutritional_values_delete'),
]
