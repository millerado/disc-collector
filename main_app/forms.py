from django.forms import ModelForm
from .models import Throws

class ThrowForm(ModelForm):
  class Meta:
    model = Throws
    fields = ('date', 'distance')