from django.forms import ModelForm
from apps.despesa.models import Despesa


class DespesaCreateForm(ModelForm):
    class Meta:
        model = Despesa
       # fields = '__all__'
        exclude = ('usuario',)

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('usuario')
        super(DespesaCreateForm, self).__init__(*args, **kwargs)

