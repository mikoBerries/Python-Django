from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import ReviewForm
from .models import Review
# Create your views here.


class ReviewView(View):
    " Populating view with django view"

    def get(self, request):
        " if incoming request method is GET"
        form = ReviewForm()
        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        " if incoming request method is POST"
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return HttpResponseRedirect("/reviews/thank-you")

        return render(request, "reviews/review.html", {
            "form": form
        })


def review(request):
    " Rendering review form"
    # if request.method == 'POST':
    #     entered_username = request.POST['username']
    #     if entered_username == "" and len(entered_username) >= 100:
    #         return render(request, "reviews/review.html", {
    #             "has_error": True
    #         })

    #     print(entered_username)

    # return render(request, "reviews/review.html")

    if request.method == 'POST':
        # filling ReviewForm class with incoming POST request
        form = ReviewForm(request.POST)

        # for updating exiting data from database

        # saved_review = Review.objects.get(pk=1)
        # form = ReviewForm(request.POST,instance=saved_review)

        # checking ReviewForm validdity
        if form.is_valid():
            # saving data using form.Froms
            # review = Review(
            #     user_name=form.cleaned_data['user_name'],
            #     review_text=form.cleaned_data['review_text'],
            #     rating=form.cleaned_data['rating'])
            # review.save()

            # saving data to form.ModelForms
            form.save()
            print(form.cleaned_data)
            return HttpResponseRedirect("/reviews/thank-you")
    else:
        form = ReviewForm()

    # form will construct as ReviewForm stated
    # form = ReviewForm()
    return render(request, "reviews/review.html", {
        "form": form
    })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
