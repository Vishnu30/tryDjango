import stripe

from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import StripeForm


class StripeMixin(object):
    def get_context_data(self, **kwargs):
        context = super(StripeMixin, self).get_context_data(**kwargs)
        context['publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


class thanks(TemplateView):
    template_name = 'thanks.html'


class checkout(StripeMixin, FormView):
    template_name = 'checkout.html'
    form_class = StripeForm
    success_url = reverse_lazy('thanks')

    def form_valid(self, form):
        stripe.api_key = settings.STRIPE_SECRET_KEY

        customer_data = {
            'description': 'Some Customer Data',
            'card': form.cleaned_data['stripe_token']
        }
        customer = stripe.Customer.create(**customer_data)
        return super(checkout, self).form_valid(form)