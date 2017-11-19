from django import template

from beers.models import Beer, Company

register = template.Library()


@register.simple_tag
def beer_counter():
    return Beer.objects.count()


@register.assignment_tag
def company_counter():
    return Company.objects.count()


@register.inclusion_tag('partials/beer_list_small.html')
def beer_list_small():
    return {'beers': Beer.objects.all()}
