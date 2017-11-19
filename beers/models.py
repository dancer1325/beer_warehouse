from django.db import models

from beers.utils import beer_image_upload_location
from core.models import CommonInfo


class Company(CommonInfo):
    name = models.CharField('Name', max_length=255)
    tax_number = models.IntegerField('Tax Number', unique=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class Beer(CommonInfo):
    COLOR_YELLOW = 1
    COLOR_AMBER = 2
    COLOR_BROWN = 3
    COLOR_BLACK = 4

    COLOR_CHOICES = (
        (COLOR_YELLOW, 'Yellow'),
        (COLOR_AMBER, 'Amber'),
        (COLOR_BROWN, 'Brown'),
        (COLOR_BLACK, 'Black')
    )

    name = models.CharField('Name', max_length=255)
    abv = models.DecimalField('Alcohol by volume', max_digits=5, decimal_places=2, default=0)
    color = models.PositiveSmallIntegerField('Color', choices=COLOR_CHOICES, default=COLOR_YELLOW)
    is_filtered = models.BooleanField("Is filtered?", default=False)
    creation_date = models.DateTimeField("Creation date", auto_now_add=True)
    image = models.ImageField("Image", blank=True, null=True, upload_to=beer_image_upload_location, max_length=400)
    company = models.ForeignKey(Company, related_name="beers")

    class Meta:
        verbose_name = "Beer"
        verbose_name_plural = "Beers"
        ordering = ['-name']

    def __str__(self):
        return self.name

    @property
    def is_alcoholic(self):
        return self.abv > 0

    def has_more_alcohol_than(self, alcohol):
        return self.abv > alcohol


class SpecialIngredient(CommonInfo):
    name = models.CharField('Name', max_length=255)
    beers = models.ManyToManyField(Beer, blank=True, related_name="special_ingredients")

    class Meta:
        verbose_name = "Special ingredient"
        verbose_name_plural = "Special ingredients"

    def __str__(self):
        return self.name