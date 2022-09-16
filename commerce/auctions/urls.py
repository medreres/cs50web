from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_listing, name="create"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("categories", views.categories, name="categories"),
    # path("categories/<str:filter>", views.search, name="search"),
    path("<int:id>/addToWatchlist", views.addToWatchlist, name="addToWatchList"),
    path("<int:id>/placeBid", views.placeBid, name="placeBid"),
    path("<int:id>/closeListing", views.closeListing, name="closeListing"),
    path("<int:id>/comment", views.makeComment, name="comment"),
    path("<int:id>", views.listing, name="listing"),
]
