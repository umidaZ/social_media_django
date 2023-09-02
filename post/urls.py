from django.urls import path
from . import views
from .views import AddCommentView

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.like_post, name='like-post'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
]