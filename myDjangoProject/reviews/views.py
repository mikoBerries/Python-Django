from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, FormView


from .forms import ReviewForm
from .models import Review
# Create your views here.


class ReviewView(CreateView):
    " Using django.CreateView for handling form template"
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "thank-you"

    # " using django formview to handle form related templates"
    # form_class = ReviewForm
    # template_name = "reviews/review.html"
    # success_url = "reviews/thank-you"

    # def form_valid(self, form):
    #     " override parent method for valid input"
    #     form.save()
    #     return super().form_valid(form)

    # def form_invalid(self, form):
    #     " override parent method for invlid input"
    #     return super().form_invalid(form)

    # " Populating view with django view"

    # def get(self, request):
    #     " if incoming request method is GET"
    #     form = ReviewForm()
    #     return render(request, "reviews/review.html", {
    #         "form": form
    #     })

    # def post(self, request):
    #     " if incoming request method is POST"
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         print(form.cleaned_data)
    #         return HttpResponseRedirect("/reviews/thank-you")

    #     return render(request, "reviews/review.html", {
    #         "form": form
    #     })


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


class ThankYouView(TemplateView):
    " Wrapper django class for static/simple template"
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        " Overrading to adding context data to template"
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


class ReviewListView(ListView):
    " fetching all reviews list using Django. Listview"
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self) -> QuerySet[Any]:
    #     query = super().get_queryset()
    #     data = query.filter(rating__gt=3)
    #     return data

    # def get_context_data(self, **kwargs):
    #     " Overrading to adding context data to template"
    #     context = super().get_context_data(**kwargs)
    #     reviews = Review.objects.all()
    #     context["reviews"] = reviews
    #     return context


class SingleReviewView(DetailView):
    " fetching single data using django DetailView using slug url pk "
    template_name = "reviews/single_review.html"
    model = Review

    # def get_context_data(self, **kwargs):
    #     " Overrading to adding context data to template"
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs["id"]
    #     selected_review = Review.objects.get(pk=review_id)
    #     context["review"] = selected_review
    #     return context
