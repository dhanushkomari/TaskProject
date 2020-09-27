from django.urls import path
from . import views

app_name = 'AppPost'

urlpatterns = [
    path('post-form',views.PostFormView,name='post-form'),
    path('post-list',views.PostList,name='post-list'),
    path('post-complete',views.PostComplete,name='post-complete'),
    path('post-delete/<str:pk>',views.PostDelete,name='post-delete'),
    path('success',views.SuccessView,name='success'),
    path('contact/',views.ContactView,name='contact')
]
