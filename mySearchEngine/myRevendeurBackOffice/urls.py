from django.urls import path
from myRevendeurBackOffice import views


urlpatterns = [
    path('infoproducts/', views.InfoProductList.as_view()),
    path('infoproduct/<int:tig_id>/', views.InfoProductDetail.as_view()),
    path('putonsale/<int:tig_id>/<str:newPrice>/', views.putOnSale.as_view()),
    path('removesale/<int:tig_id>/', views.removesale.as_view()),
    path('incrementStock/<int:tig_id>/<int:addstock>/', views.incrementStock.as_view()),
    path('decrementStock/<int:tig_id>/<int:lessstock>/', views.decrementStock.as_view()),
    path('updatePrice/<int:tig_id>/<int:newPrice>/', views.updatePrice.as_view()),
    path('stats/', views.ReadJsonView.as_view()),
    path('poissons/', views.PoissonsList.as_view()),
    path('newOperation/<int:category>/<str:type>/<int:stock>/<int:priceOperation>/', views.newOperation.as_view()),
]
