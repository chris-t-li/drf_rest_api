
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import (
    WatchlistAV, WatchDetailAV, ReviewList, ReviewDetail, ReviewCreate, StreamPlatformVS, UserReview, WatchListGV)

router = DefaultRouter()
router.register('stream', StreamPlatformVS,
                basename='streamplatform')

urlpatterns = [
    path('list/', WatchlistAV.as_view(), name="watchlist"),
    path('<int:movie_id>', WatchDetailAV.as_view(), name='movie-detail'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name="review-list"),
    path('review/<int:pk>/', ReviewDetail.as_view(), name="review-detail"),
    path('<int:pk>/review-create/',
         ReviewCreate.as_view(), name="review-create"),
    path('', include(router.urls)),

    path('reviews/', UserReview.as_view(), name='user-review-detail'),
    path('list2/', WatchListGV.as_view(), name='watch-list'),
    # path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
]

# # path('stream/', StreamPlatformAV.as_view(), name="stream-platforms"),
# # path('stream/<int:pk>',
# #  StreamPlatformDetailAV.as_view(), name="streamplatform-detail"),
# # path('review/', ReviewList.as_view(), name='review-list'),
