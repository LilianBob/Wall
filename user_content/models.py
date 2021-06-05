from django.db import models
from reg_login.models import User

# Create your models here.
class WallMessageManager(models.Manager):
    def validate_wallMessage(self, wall_message):
        errors = {}
        if len(wall_message) < 2:
            errors['length'] = 'wallMessages must be at least 2 characters'
        if len(wall_message) > 255:
            errors['length'] = 'wallMessages take a max of 255 characters'
        return errors

class WallMessage(models.Model):
    content = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name='wallMessages', on_delete=models.CASCADE)
    # user_likes = models.ManyToManyField(User, related_name='liked_posts')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    objects= WallMessageManager()

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    wallMessage = models.ForeignKey(WallMessage, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
