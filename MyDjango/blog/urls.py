from django.urls import path
from .views import *

app_name='blog'

urlpatterns = [
    path('<int:post_id>/share/', post_share, name="post_share"),
    path('', PostListView.as_view(), name= 'post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>', post_detail, name='post_detail' )
]