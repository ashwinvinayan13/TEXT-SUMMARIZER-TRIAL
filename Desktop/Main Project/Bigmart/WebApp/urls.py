from django.urls import path
from WebApp import views


urlpatterns = [

    path('User_Login/', views.User_Login, name='User_Login'),
    path('User_registration/', views.User_registration, name='User_registration'),
    path('user_login/', views.user_login, name='user_login'),
    path('Home/', views.HomePage, name='Home'),
    path('About/', views.About, name='About'),
    path('Contact/', views.Contact, name='Contact'),
    path('Save_Contact/', views.Save_Contact, name='Save_Contact'),
    path('All_Products/', views.All_Products, name='All_Products'),
    path('Filter_Products/<ct_name>/', views.Filter_Products, name='Filter_Products'),
    path('Single_Product/<int:p_id>/', views.Single_Product, name='Single_Product'),
    path('Save_User/', views.Save_User, name='Save_User'),
    path('User_Logout/', views.User_Logout, name='User_Logout'),
    path('cart/', views.Cart, name='cart'),
    path('SaveCart/', views.SaveCart, name='SaveCart'),
    path('Delete_cart/<int:cr_id>/', views.Delete_cart, name='Delete_cart'),
    path('Checkout', views.Checkout, name='Checkout'),
    path('Save_order', views.Save_order, name='Save_order'),
    path('Getaway', views.Getaway, name='Getaway')




]
