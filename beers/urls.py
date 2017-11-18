from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from beers.views import landing_view, BeerListView, BeerDetailView, CompanyUpdateView, CompanyListView, CompanyCreateView

urlpatterns = [
    url(r'^$', login_required(landing_view), name='landing-view'),
    url(r'^beer/list/$', login_required(BeerListView.as_view()), name='beer-list-view'),
    url(r'^beer/detail/(?P<pk>\d+)/$', login_required(BeerDetailView.as_view()), name='beer-detail-view'),

    url(r'^company/list/$', login_required(CompanyListView.as_view()), name='company-list-view'),
    url(r'^company/create/$', login_required(CompanyCreateView.as_view()), name='company-create-view'),
    url(r'^company/edit/(?P<pk>\d+)/$', login_required(CompanyUpdateView.as_view()), name='company-edit-view'),
]