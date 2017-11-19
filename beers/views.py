from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.forms.formsets import formset_factory

# Create your views here.
from beers.forms import CompanyForm, BeerFormset
from beers.mixins import AddMyBirthdayToContextMixin
from beers.models import Beer, Company


def landing_view(request):
    request.session['counter'] = request.session.get('counter', 0) + 1
    everybody_value = "todas"
    context = {
        'everybody_var': everybody_value,
        'my_list': [1, 3, 88889],
        'counter': request.session['counter']
    }

    return render(request, 'beers.html', context)


class BeerListView(ListView):
    model = Beer


class BeerDetailView(AddMyBirthdayToContextMixin, DetailView):
    model = Beer


class CompanyListView(ListView):
    model = Company


# Form
# def company_edit_view(request, pk):
#     company = get_object_or_404(Company, pk=pk)
#
#     if request.method == 'GET':
#         form = CompanyForm(initial={
#             'name': company.name,
#             'tax_num': company.tax_number
#         })
#     else:
#         # print(request.POST)
#         form = CompanyForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             company.name = form.cleaned_data['name']
#             company.tax_number = form.cleaned_data['tax_num']
#             company.save()
#
#     context = {
#         'company': company,
#         'form': form
#     }
#
#     return render(request, 'company/company_form.html', context)


# ModelForm
# def company_edit_view(request, pk):
#     company = get_object_or_404(Company, pk=pk)
#
#     if request.method == 'GET':
#         form = CompanyForm(instance=company)
#     else:
#         form = CompanyForm(request.POST, instance=company)
#         if form.is_valid():
#             form.save()
#
#     context = {
#         'company': company,
#         'form': form
#     }
#
#     return render(request, 'company/company_form.html', context)


class CompanyUpdateView(UpdateView):
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('company-list-view')


class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'beers/company_create_with_beers.html'
    success_url = reverse_lazy('company-list-view')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['beer_formset'] = BeerFormset(self.request.POST)
        else:
            data['beer_formset'] = BeerFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        beer_formset = context['beer_formset']

        if beer_formset.is_valid():
            self.object = form.save()
            beer_formset.instance = self.object
            beer_formset.save()

        return super().form_valid(form)