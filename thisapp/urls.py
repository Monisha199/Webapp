from django.urls import path
from . import views


urlpatterns=[
    path('', views.Home),
    # path('appadmin', views.Appadmin),
    path('user/',views.UserList.as_view()),
    path('user/<int:pk>/', views.UserUpdate.as_view()),
    path('group/', views.GroupDetails.as_view()),
    path('group/<int:pk>/', views.GroupUpdate.as_view()),
    path('group/members/<int:pk>',views.GroupMemberInfo.as_view()),
    path('login',views.Login),
    path('new_user', views.new_user),
    path('chat/',views.chatroom),
    path('chat/check_group',views.check_group),
    path('<str:room>/', views.group_exists),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('<str:room>/logout.html',views.exit)]