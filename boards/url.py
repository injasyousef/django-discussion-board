from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.BoardListView.as_view(), name='home'),
    path('about/',views.about,name='about'),
    path('boards/<int:board_id>/',views.board_topics,name='board_topics'),
    path('boards/<int:board_id>/new/',views.new_topic,name='new_topic'),
    path('boards/<int:board_id>/topics/<int:topic_id>', views.topics_posts, name='topics_posts'),
    path('boards/<int:board_id>/topics/<int:topic_id>/reply', views.reply_topic, name='reply_topic'),
    path('boards/<int:board_id>/topics/<int:topic_id>/posts/<int:post_id>/edit', views.PostUpdateView.as_view(), name='edit_post'),

]
