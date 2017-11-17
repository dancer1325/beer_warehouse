from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from beers.views import landing_view, BeerListView, BeerDetailView

urlpatterns = [
    url(r'^$', login_required(landing_view), name='landing-view'),
    url(r'^beer/list/$', login_required(BeerListView.as_view()), name='beer-list-view'),
    url(r'^beer/detail/(?P<pk>\d+)/$', login_required(BeerDetailView.as_view()), name='beer-detail-view'),
]