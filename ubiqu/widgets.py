from django.forms import MultiWidget, MultiValueField, DateTimeField
from collections import namedtuple
from datetimewidget.widgets import DateTimeWidget
import uuid


# for now, assume no functionality for a time interval
DateTimeInterval = namedtuple('DateTimeInterval', 'start_date end_date')


class DateTimeIntervalMultiField(MultiValueField):

    def __init__(self, *args, **kwargs):

        # set the right widgets in DateTimeIntervalWidget
        fields = (DateTimeField(), DateTimeField())
        super(DateTimeIntervalMultiField, self).__init__(fields, *args, **kwargs)
        # in django 1.5 the widget argument to MultiValueField.__init__ does nothing
        self.widget = kwargs.get('widget') or DateTimeIntervalWidget()

    def compress(self, data_list):
        return DateTimeInterval(*data_list)


class DateTimeIntervalWidget(MultiWidget):

    def __init__(self, attrs=None, options=None, id=None, usel10n=None):
        if id is None:
            id = str(uuid.uuid4())
        widgets = (DateTimeWidget(attrs, options, id + '_startdate', usel10n),
                   DateTimeWidget(attrs, options, id + '_enddate', usel10n))
        super(DateTimeIntervalWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if isinstance(value, DateTimeInterval):
            return [value.start_date, value.end_date]
        else:
            return [None, None]

    def format_output(self, rendered_widgets):
        return ''.join(rendered_widgets)

