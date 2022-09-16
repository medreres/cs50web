import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.utils import timezone
from .models import User, Post
from .forms import NewPost


def getPosts(request):      # load posts via AJAX

    pageInd = request.GET['page']

    # get all the posts
    posts = Post.objects.order_by('-id').all()
    # convert them into pages
    pages = Paginator(posts, 10)

    # get page with required index
    try:
        page = pages.page(pageInd)
    except:
        # TODO
        return JsonResponse({'ERROR': "Page not found 404"})

    # get posts the user liked
    postLiked = Post.objects.filter(likes__id=request.user.id)
    posts = []
    for post in page.object_list:
        # serialize the posts
        postSeriailzed = post.serialize()

        # add boolean whether the post is liked
        postSeriailzed['isLiked'] = post in postLiked

        # add to the list
        posts.append(postSeriailzed)
    return JsonResponse({'posts': posts,
                         'lastPage': pages.num_pages}, safe=False)


def getUserPosts(request, username):  # load posts posted by the user
    pageInd = request.GET['page']

    # get all the posts
    posts = Post.objects.order_by(
        '-id').filter(author=User.objects.get(username=username)).all()
    # convert them into pages
    pages = Paginator(posts, 10)

    # # quantity of posts
    # postsCount = posts.count()

    # # quantity of followers
    # # TODO
    # followers = 0

    # # quantity of people the user is following
    # # TODO
    # following = 0

    # get page with required index
    try:
        page = pages.page(pageInd)
    except:
        # TODO
        return JsonResponse({'ERROR': "Page not found 404"})

    # get posts the user liked
    postLiked = Post.objects.filter(likes__id=request.user.id)
    posts = []
    for post in page.object_list:
        # serialize the posts
        postSeriailzed = post.serialize()

        # add boolean whether the post is liked
        postSeriailzed['isLiked'] = post in postLiked

        # add to the list
        posts.append(postSeriailzed)

    return JsonResponse({'posts': posts,
                         'lastPage': pages.num_pages, }, safe=False)


@login_required
def getFollowing(request):
    # get all the users we follow
    followingUsers = User.objects.filter(followers__id=request.user.id)

    # get all the posts from that users
    posts = Post.objects.order_by('-id').filter(author__in=followingUsers)

    # break into pages
    pages = Paginator(posts, 10)

    # get page index
    pageInd = request.GET['page']

    # loag the required page
    try:
        page = pages.page(pageInd)
    except:
        # TODO
        return JsonResponse({'ERROR': "Page not found 404"})

    # get posts the user liked
    postLiked = Post.objects.filter(likes__id=request.user.id)
    posts = []
    for post in page.object_list:
        # serialize the posts
        postSeriailzed = post.serialize()

        # add boolean whether the post is liked
        postSeriailzed['isLiked'] = post in postLiked

        # add to the list
        posts.append(postSeriailzed)

    return JsonResponse({'posts': posts,
                         'lastPage': pages.num_pages}, safe=False)


def following(request):

    # get page index
    try:
        pageInd = request.GET['page']
    except:
        pageInd = 1
    return render(request, 'network/following.html', {
        'filter': 'following',
        'pageInd': pageInd
    })


def index(request):
    # get page index
    try:
        pageInd = request.GET['page']
    except:
        pageInd = 1

    return render(request, "network/index.html", {
        'NewPostForm': NewPost(),
        'pageInd': pageInd,
        'filter': 'all'
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


@csrf_exempt
@login_required
def makePost(request):
    # method must be POST
    if request.method != 'POST':
        return JsonResponse({'error': 'Method is not Post'}, status=400)

    # get data
    body = json.loads(request.body)
    post = Post(author=request.user,
                body=body['body'], timestamp=timezone.now())
    post.save()
    return JsonResponse({'message': 'Post successfully saved'}, status=200)


def profile(request, username):
    # get the user's profile
    try:
        user = User.objects.get(username=username)
    except:
        return HttpResponse("User doesn't exist!")

    # display button for following
    try:
        user.followers.get(username=request.user)
        isFollowing = True
    except:
        isFollowing = False

    # get quantity of posts
    postsCount = Post.objects.order_by('-id').filter(author=user).all().count()

    # quantity of followers
    followersCount = user.followers.count()

    # quantity of following
    followingCount = user.following.count()

    # get page index
    try:
        pageInd = request.GET['page']
    except:
        pageInd = 1
    return render(request, 'network/profile.html', {
        'pageInd': pageInd,
        'postsCount': postsCount,
        'followersCount': followersCount,
        'followingCount': followingCount,
        'username': username,
        'isFollowing': isFollowing,
        'filter': 'self',
    })


@login_required
def follow(request, username):
    if request.user.username == username:
        return HttpResponse('error')
    # add to user's followers
    userToFollow = User.objects.get(username=username)
    userToFollow.followers.add(request.user)
    userToFollow.save()

    # add to the user following
    userFollowed = User.objects.get(username=request.user)
    userFollowed.following.add(userToFollow)
    userFollowed.save()
    return HttpResponse('followed successfully!')


@login_required
def unfollow(request, username):
    if request.user.username == username:
        return HttpResponse('error')

    # remove from the user's followers
    userToUnfollow = User.objects.get(username=username)
    userToUnfollow.followers.remove(request.user)
    userToUnfollow.save()

    # remove from following
    userUnfollowed = User.objects.get(username=request.user)
    userUnfollowed.following.remove(userToUnfollow)
    userUnfollowed.save()
    return HttpResponse('unfollowed successfully!')


@csrf_exempt
@login_required
def editPost(request, id):
    # check if the author is trying to edit the post
    post = Post.objects.get(pk=id)
    if post.author != request.user:
        return JsonResponse({'error': "It's not your post!"})

    # method must be post
    if request.method != 'POST':
        return JsonResponse({'error': "Wrong method"})

    # get the post , edit the body and save
    body = json.loads(request.body)
    post.body = body['body']
    post.save()
    return JsonResponse({'message': "zbs"})


@csrf_exempt
@login_required
def likePost(request, id):
    if request.method != 'POST':
        return JsonResponse({"error": 'Incorrect method'})

    if not request.user.is_authenticated:
        return JsonResponse({'error': 'authenticate'})

    # get model of user
    user = request.user

    # get that post and add user to likes manytomanyfields
    post = Post.objects.get(pk=id)
    post.likes.add(user)
    post.save()

    # add this post to the user's manytomany rel for likes
    user.liked.add(post)
    user.save()

    return JsonResponse({'message': 'liked successfully!'})


@csrf_exempt
@login_required
def dislikePost(request, id):
    if request.method != 'POST':
        return JsonResponse({"error": 'Incorrect method'})

    if not request.user.is_authenticated:
        return JsonResponse({'error': 'authenticate'})

    # get model of user
    user = request.user

    # get that post and add user to likes manytomanyfields
    post = Post.objects.get(pk=id)
    post.likes.remove(user)
    post.save()

    # add this post to the user's manytomany rel for likes
    user.liked.remove(post)
    user.save()

    return JsonResponse({'message': 'disliked successfully!'})


@login_required
def isLiked(request, id):
    # check the method
    if request.method != 'GET':
        return JsonResponse({'error': 'Wrong method'})

    # check if user is logged
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Not authenticated'})

    # check if user liked the post
    post = Post.objects.get(pk=id)
    try:
        post.likes.get(username=request.user)
        isLiked = 'true'
    except:
        isLiked = 'false'

    return JsonResponse({'message': isLiked})
