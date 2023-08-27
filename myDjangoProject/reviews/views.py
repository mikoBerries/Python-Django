from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm
from .models import Review
# Create your views here.


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
        # filling ReviewForm class with incoming POST reqeust
        form = ReviewForm(request.POST)

        # checking ReviewForm validdity
        if form.is_valid():
            review = Review(
                user_name=form.cleaned_data['user_name'],
                review_text=form.cleaned_data['review_text'],
                rating=form.cleaned_data['rating'])
            review.save()
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
