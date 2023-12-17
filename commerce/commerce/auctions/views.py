from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import ListingForm


from .models import User, Listing


def index(request):
    listings = Listing.objects.all()
    return render(request, "auctions/index.html", {
        "listings" : listings
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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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



@login_required
def create(request):
    if request.method=="POST":
        newListing = Listing(
            title=request.POST["title"],
            description=request.POST["description"],
            categories=request.POST["categories"],
            imageURL=request.POST["imageURL"]
        )
        newListing.save()
        return index(request)
    else:
        form = ListingForm()
        return render(request, "auctions/create.html", {"form" : form})
    
    


def loadListing(request, title):
    titles = [listing.title for listing in Listing.objects.all()]
    if (title in titles):
        listing = Listing.objects.get(title=title)
        return render(request, "auctions/listing.html",  {"listing" : listing} )
    else :
        return render(request, "auctions/404.html")
    