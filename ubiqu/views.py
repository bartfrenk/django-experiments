from django.views import generic
from ubiqu.forms import DateTimeIntervalForm
from django.http import HttpResponseRedirect


class DateTimeIntervalView(generic.edit.FormView):
    form_class = DateTimeIntervalForm
    template_name = 'datetimeinterval.html'

    def form_valid(self, form):
        # data = form.cleaned_data
        return HttpResponseRedirect('dates')
