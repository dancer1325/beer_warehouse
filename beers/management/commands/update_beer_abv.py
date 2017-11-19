from django.core.management.base import BaseCommand, CommandError

from beers.models import Beer


class Command(BaseCommand):

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('abv_desired',
                            nargs=1,  # number of args.
                            type=int)

        # Named (optional) arguments
        parser.add_argument(
            '--fake',
            action='store_true',  # This stores True if argument is found
            dest='fake',  # The name of the attribute to be added to the object returned by parse_args()
            default=False,  # The value produced if the argument is absent from the command line
            help='Do not apply any change',
        )

    def handle(self, *args, **options):
        #print("options", options)

        abv_desired = options.get('abv_desired', None)
        if len(abv_desired) > 1:
            # careful! positional args are collected in a list
            # If we keep nargs=1, won't happen anyway
            raise CommandError("Too many abvs!")

        if abv_desired:
            abv_desired = abv_desired[0]

        #print("ABV", abv_desired)

        if abv_desired and not options['fake']:
            print("All changes applied")
            for beer in Beer.objects.all():
                beer.abv = abv_desired
                beer.save()
        else:
            print("No changes applied")