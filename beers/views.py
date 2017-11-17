from django.views.generic import ListView, DetailView
from django.shortcuts import render

# Create your views here.
from beers.mixins import AddMyBirthdayToContextMixin
from beers.models import Beer, Company


def landing_view(request):
    # return HttpResponse("Saludos")

    everybody_value = "todas"
    context = {
        'everybody_var': everybody_value,
        'my_list': [1, 3, 88889]
    }

    return render(request, 'beers.html', context)


class BeerListView(ListView):
    model = Beer


class BeerDetailView(AddMyBirthdayToContextMixin, DetailView):
    model = Beer