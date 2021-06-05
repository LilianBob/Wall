from typing import Text
from django.shortcuts import render, redirect
from .models import WallMessage, Comment
from reg_login.models import User
from django.contrib import messages

## Rendering Views
def post_content(request):
    content = request.POST['content']
    errors = WallMessage.objects.validate_wallMessage(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/process_content')
    WallMessage.objects.create(content= content, poster= User.objects.get(id= request.session['user_id']))
    return redirect(f'/success')

def post_comment(request, wallMessage_id):
    # wallMessage_id = request.POST['wallMessage_id']
    comment= request.POST['comment']
    poster = User.objects.get(id= request.session['user_id'])
    wallMessage = WallMessage.objects.get(id= wallMessage_id)
    Comment.objects.create(comment= comment, poster= poster, wallMessage= wallMessage)
    return redirect('/success')

def profile(request, user_id):
    context = {
        'user': User.objects.get(id= user_id)
    }
    return render(request, 'profile.html', context)

# def add_like(request, id):
#     liked_message = WallMessage.objects.get(id=id)
#     user_liking = User.objects.get(id=request.session['user_id'])
#     liked_message.user_likes.add(user_liking)
#     return redirect('/success')

def delete_comment(request, comment_id):
    destroyed = Comment.objects.get(id=comment_id)
    destroyed.delete()
    return redirect('/success')

def edit(request, user_id):
    edit_user = User.objects.get(id=user_id)
    edit_user.first_name = request.POST['fname']
    edit_user.last_name = request.POST['lname']
    edit_user.email = request.POST['email']
    edit_user.save()
    return redirect('/success')
