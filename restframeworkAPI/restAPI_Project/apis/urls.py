from django.urls import path,include
from .import views
from rest_framework.urlpatterns import format_suffix_patterns #type:ignore
urlpatterns = [
    path('list/',views.movieList.as_view(),name = "movie_list"),
    path('list/<int:pk>',views.movieDetail.as_view(),name = "movie_detail"),
    # path('stream/',views.stream_list,name = "stream-platform"),
    # path('stream/<int:pk>',views.stream_detail,name = "stream-platform-detail")
    path('stream/',views.streamPlatformList.as_view(), name = "stream-platform"),
    path('stream/<int:pk>',views.streamPlatformDetail.as_view(), name = "stream-platform-detail")
    ]

urlpatterns = format_suffix_patterns(urlpatterns)