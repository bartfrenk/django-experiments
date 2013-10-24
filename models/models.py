
from django.db import models

mdls = []

def listener(sender, **kwargs):
    global str
    mdls.append('%s.%s' % (sender._meta.app_label, sender._meta.object_name))

models.signals.class_prepared.connect(listener)


class TestField(models.Field):

    def contribute_to_class(self, cls, name):
        setattr(cls, name, (self, cls))
        self.name = name


class IntervalField(models.Field):

    Orderable = models.IntegerField

    def contribute_to_class(self, cls, name):
        setattr(cls, "lower_" + name, self.Orderable())
        setattr(cls, "upper_" + name, self.Orderable())


class ComplexModel(models.Model):
    test = TestField()
    interval = IntervalField()
    number = models.IntegerField()

class X(models.Model):
    pass
