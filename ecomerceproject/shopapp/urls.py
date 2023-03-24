from django . urls import path
from.import views
app_name = 'shopapp'

urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat, name="pro_by_cat"),
    path('<slug:c_slug>/<slug:product_slug>/', views.ProDetail, name='ProDetail')
]