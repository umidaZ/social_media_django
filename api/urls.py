from django.urls import path
from .views import *


# urlpatterns = [
#     # path('<int:id>/delete', RetriveProfile.as_view()),
#     # path('<int:id>/update', RetriveProfile.as_view()),
#     # path('<int:id>/', RetriveProfile.as_view()),
#     # path('', ShowProfiles.as_view()),
#
# ]

urlpatterns=[
    path('', ProfileViewSet.as_view()),
    path('prof_create/', CreateProfile.as_view()),
    path('<int:pk>/prof_edit/', Editprofile.as_view()),
    path('post_create/', CreatePost.as_view()),
    path('<int:pk>/post_edit/', EditPost.as_view()),
    path('all_posts', AllPost.as_view()),

]