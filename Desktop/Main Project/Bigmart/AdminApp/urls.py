from django.urls import path
from AdminApp import views


urlpatterns=[

    path('index/', views.index, name='index_page'),
    path('AddCategory/', views.AddCategory, name='AddCategory'),
    path('Save_Category/', views.Save_Category, name='Save_Category'),
    path('Display_Category/', views.Display_Category, name='Display_Category'),
    path('Edit_Category/<int:pro_id>/', views.Edit_Category, name='Edit_Category'),
    path('Update_Category/<int:pro_id>/', views.Update_Category, name='Update_Category'),
    path('Delete_Category/<int:pro_id>/', views.Delete_Category, name='Delete_Category'),
    path('AddProducts/', views.AddProducts, name='AddProducts'),
    path('Save_Products/', views.Save_Products, name='Save_Products'),
    path('Display_Products/', views.Display_Products, name='Display_Products'),
    path('EditProduct/<int:pro_id>/', views.EditProduct, name='EditProduct'),
    path('UpdateProduct/<int:pro_id>/', views.UpdateProduct, name='UpdateProduct'),
    path('DeleteProduct/<int:pro_id>', views.DeleteProduct, name='DeleteProduct'),
    path('Admin_login_page/', views.Admin_login_page, name='Admin_login_page'),
    path('Admin_login/', views.Admin_login, name='Admin_login'),
    path('Admin_Logout/', views.Admin_Logout, name='Admin_Logout'),
    path('View_Contact/', views.View_Contact, name='View_Contact'),
    path('Delete_Contact/<int:p_id>/', views.Delete_Contact, name='Delete_Contact'),
    path('View_Message/', views.View_Message, name='View_Message'),
    path('Delete_Message/<int:p_id>/', views.Delete_Message, name='Delete_Message'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('Delete_cart/<int:d_id>/', views.Delete_cart, name='Delete_cart'),
    path('View_order/', views.View_order, name='View_order'),
    path('Delete_order/<int:de_id>/', views.Delete_order, name='Delete_order'),


]