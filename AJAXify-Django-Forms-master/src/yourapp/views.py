# yourapp.views.py

from django.views.generic import FormView

from .forms import JoinForm


class JoinFormView(FormView):
    form_class = JoinForm
    template_name = 'forms/ajax.html'
    success_url = '/form-success/'
