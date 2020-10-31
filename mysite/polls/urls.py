from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.user_login, name='loginpage'),
    path('logout/', views.user_logout, name='logout'),
    path('<int:pk>/', views.valid_vote, name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    
]