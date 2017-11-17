from django.views.generic import ListView
from django.shortcuts import render

# Create your views here.
from beers.models import Beer, Company


def first_view(request):
    # return HttpResponse("Saludos")

    everybody_value = "todas"
    context = {
        'everybody_var': everybody_value,
        'my_list': [1, 3, 88889]
    }

    return render(request, 'beers.html', context)

class ListBeerView(ListView):
    model = Beer

def beer_detail_view(request, pk):
    return render(request, 'beer_detail.html', {'beer': Beer.objects.get(pk=pk)})