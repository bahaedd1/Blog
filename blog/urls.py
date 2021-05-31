from django.urls import path,include
from . import views
urlpatterns =[
    path('',views.index,name="login"),
    path('register',views.register,name="register"),
    path('home',views.home,name = "home"),
    path('logout',views.logout,name="logout"),
    path('bl',views.addArticle,name="bl"),
    path('<id>',views.console,name="blogId"),
    path('delete/<id>',views.delete,name="delete"),
    path('edit/<id>',views.edit,name="edit")
]