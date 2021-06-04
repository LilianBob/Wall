from django.urls import path
from . import views

urlpatterns = [
    path('process_message', views.post_content),
    path('add_comment/<int:id>', views.post_comment),
    path('user_profile/<int:id>', views.profile),
    path('like/<int:id>', views.add_like),
    path('delete/<int:id>', views.delete_comment),
    path('edit/<int:id>', views.edit),
]