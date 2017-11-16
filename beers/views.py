from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def first_view(request):
    # return HttpResponse("Saludos")

    everybody_value = "todas"
    context = {
        'everybody_var': everybody_value,
        'my_list': [1, 3, 88889]
    }

    return render(request, 'beers.html', context)

