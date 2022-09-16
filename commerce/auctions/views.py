from email import message
from nis import cat
import re
from unicodedata import category
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from httplib2 import Authentication
from .forms import CreateListing, LoginForm, MakeBid, MakeComment
from .models import AuctionListing, Bid, User, WatchList, Comment
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages
from commerce.settings import CATEGORIESCHOICES


def index(request):
    listings = AuctionListing.objects.all()
    if request.user.is_authenticated:
        WatchListSize = WatchList.objects.filter(author=request.user)
        return render(request, "auctions/index.html", {
            'listings': listings,
            'WatchListSize': WatchListSize.count(),
        })
    else:
        return render(request, "auctions/index.html", {
            'listings': listings,
        })


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(
                request, username=username, password=password)

            # Check if authentication successful
            if user is not None:
                login(request, user)
                next = request.POST.get('next', '/')
                # print(next)
                return HttpResponseRedirect('/')
                return HttpResponseRedirect(reverse("index"))
            else:
                messages.error(request, 'Invalid username and/or password')
                return render(request, "auctions/login.html", {
                    "form": LoginForm()
                })
        else:
            messages.warning(request, 'Some fields are blank')
            return render(request, "auctions/login.html", {
                "form": LoginForm()
            })
    else:
        form = LoginForm()
        return render(request, "auctions/login.html", {'form': form})


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create_listing(request):

    if request.method == 'POST':
        form = CreateListing(request.POST)
        if form.is_valid():
            listing = AuctionListing()
            listing.author = request.user
            listing.title = form.cleaned_data['title']
            listing.description = form.cleaned_data['description']
            listing.date = datetime.datetime.now()
            listing.price = form.cleaned_data['price']
            listing.image = form.cleaned_data['img']
            listing.category = form.cleaned_data['category']
            listing.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/create.html", {
                'form': form
            })
    else:
        form = CreateListing()
        return render(request, "auctions/create.html", {
            'form': form
        })


def listing(request, id):
    try:
        listing = AuctionListing.objects.get(pk=id)
        try:
            is_favorite = WatchList.objects.get(
                author=request.user, listing=listing)
            is_favorite = True
        except:
            is_favorite = False

        # geting comments
        comments = Comment.objects.filter(listing=id)
        bids = Bid.objects.filter(listing=id).count
    except:
        return render(request, "auctions/listing.html", {
            'ErrorMessage': "Page doesn't exits!"
        })
    return render(request, "auctions/listing.html", {
        "listing": listing,
        "is_favorite": is_favorite,
        "BidForm": MakeBid(),
        "Bids": bids,
        "CommentForm": MakeComment(),
        "comments": comments,
    })


@login_required
def addToWatchlist(request, id):
    user = request.user
    profile = User.objects.get(pk=user.id)
    listing = AuctionListing.objects.get(pk=id)
    try:
        favorite = WatchList.objects.get(author=user, listing=listing)
        favorite.delete()
        profile.WatchListSize = int(profile.WatchListSize) - 1

    except:
        favorite = WatchList(author=user, listing=listing)
        favorite.save()
        profile.WatchListSize = int(profile.WatchListSize) + 1
    profile.save()
    return HttpResponseRedirect(reverse('listing', args=(id,)))


@login_required
def watchlist(request):
    listOfFavorites = WatchList.objects.filter(
        author=request.user.id).values_list('listing', flat=True)
    watchlist = AuctionListing.objects.filter(pk__in=listOfFavorites)
    return render(request, 'auctions/watchlist.html', {
        'watchlist': watchlist,
    })


@login_required
def placeBid(request, id):
    bid = MakeBid(request.POST)
    listing = AuctionListing.objects.get(pk=id)
    if bid.is_valid():
        if bid.cleaned_data['price'] <= listing.price:
            messages.error(request, "Bid is below the stated price")
            return HttpResponseRedirect(reverse('listing', args=(id,)))
        else:
            placedBid = Bid(author=request.user, listing=AuctionListing.objects.get(pk=id),
                            price=bid.cleaned_data['price'], date=datetime.datetime.now())
            listing = AuctionListing.objects.get(pk=id)
            listing.price = placedBid.price
            listing.winner = request.user
            listing.save()
            placedBid.save()
            messages.success(request, "Bid is placed successfully!")
            return HttpResponseRedirect(reverse('listing', args=(id,)))
    else:
        messages.warning(request, "Something went wrong")
        return HttpResponseRedirect(reverse('listing', args=(id,)))


@login_required
def closeListing(request, id):
    listing = AuctionListing.objects.get(pk=id)
    listing.isClosed = True
    listing.save()
    return HttpResponseRedirect(reverse('listing', args=(id,)))


@login_required
def makeComment(request, id):
    commentText = MakeComment(request.POST)
    if commentText.is_valid():
        commentText = commentText.cleaned_data['text']
        comment = Comment(author=request.user, listing=AuctionListing.objects.get(
            pk=id), text=commentText)
        comment.save()
    else:
        messages.warning(request, "Something went wrong")
    return HttpResponseRedirect(reverse('listing', args={id, }))


def categories(request):
    Category = request.GET.get('Category')  # getting query from the user
    print("DEBUG")
    print(Category)
    if Category is None:  # if there is no request
        listings = AuctionListing.objects.all()
        return render(request, "auctions/Category.html", {
            "categories": CATEGORIESCHOICES,
            "listings": listings,
        })
    # processing the query
    else:
        if len(Category) == 0:
            listings = AuctionListing.objects.all()
            return render(request, "auctions/Category.html", {
                "categories": CATEGORIESCHOICES,
                "listings": listings,
            })
        else:
            listings = AuctionListing.objects.filter(category=Category)
            all = AuctionListing.objects.all()
            return render(request, "auctions/Category.html", {
                "categories": CATEGORIESCHOICES,
                "listings": listings,
            })


# def search(request, filter):
#     return HttpResponse("LOL")
