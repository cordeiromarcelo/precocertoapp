from django.urls import path
from . import views

app_name = "principal"

urlpatterns = [
    path('', views.index, name='index'),
    path('dash/', views.dash, name='dash'),
    path('imports/', views.imports, name='imports'),


 #   path('<int:question_id>/', views.detail, name='detail'),
 #   path('<int:question_id>/results/', views.results, name='results'),
 #   path('<int:question_id>/vote/', views.vote, name='vote'),
]