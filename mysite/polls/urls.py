from django.urls import
from . import views
urlpatterns = [

    path(r'^$', views.index, name="index"),
    path(r'^(?P<question_id>[0-9]+)$', views.detail, name="detail"),
    path(r'^(?P<question_id>[0-9]+)/results$', views.results, name="results"),
    path (r'^(?P<question_id>[0-9]+)/vote$', views.vote, name="vote")
]
