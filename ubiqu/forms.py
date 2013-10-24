from django import forms
from datetimewidget.widgets import DateTimeWidget
# from datetime import datetime
# from widgets import DateTimeIntervalMultiField


class DateTimeIntervalForm(forms.Form):
    start_datetime = forms.DateTimeField(widget=DateTimeWidget(id='start_datetime',
                                                               attrs={'before': 'end_datetime'}))
    middle_datetime = forms.DateTimeField(widget=DateTimeWidget(id='middle_datetime',
                                                                attrs={'after': 'start_datetime', 'before': 'end_datetime'}))
    end_datetime = forms.DateTimeField(widget=DateTimeWidget(id='end_datetime'))
