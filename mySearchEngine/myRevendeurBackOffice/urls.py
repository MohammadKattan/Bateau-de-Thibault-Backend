from django.urls import path
from myRevendeurBackOffice import views

urlpatterns = [
    path('infoproducts/', views.InfoProductList.as_view()),
    path('infoproduct/<int:tig_id>/', views.InfoProductDetail.as_view()),
    path('putonsale/<int:tig_id>/<str:newPrice>/', views.putOnSale.as_view()),
    path('removesale/<int:tig_id>/', views.removesale.as_view()),
    path('incrementStock/<int:tig_id>/<int:addstock>/', views.incrementStock.as_view()),
    path('decrementStock/<int:tig_id>/<int:lessstock>/', views.decrementStock.as_view()),
    path('stats/', views.ReadJsonView.as_view()),
    path('create-admin-user/', views.CreateAdminUserView.as_view(), name='create_admin_user'),
    path('register/', views.RegisterView.as_view(), name='register'), 

]
