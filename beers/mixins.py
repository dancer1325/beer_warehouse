
class AddMyBirthdayToContextMixin(object):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['birthday'] = "mi cumple es el 14 de abril"
        return context