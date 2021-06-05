from django.urls import path
from . import views

urlpatterns = [
    path('process_content', views.post_content),
    path('add_comment/<int:wallMessage_id>', views.post_comment),
    path('user_profile/<int:wallMessage.poster.id>', views.profile),
    # path('like/<int:id>', views.add_like),
    path('delete/<int:comment_id>', views.delete_comment),
    path('edit/<int:user_id>', views.edit),
]