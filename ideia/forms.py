from django.forms import ModelForm
from .models import Ideia


class IdeiaForm(ModelForm):
    class Meta:
        model = Ideia
        fields = ['Nome','Sobrenome','Nova_ideia','Descricao','Viabilidade','Situacao','Data']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Nome'].widget.attrs['placeholder'] = 'Nome'
        self.fields['Sobrenome'].widget.attrs['placeholder'] = 'Sobrenome'
        self.fields['Nova_ideia'].widget.attrs['placeholder'] = 'Nova Ideia'
        self.fields['Descricao'].widget.attrs['placeholder'] = 'Descrição'
        self.fields['Viabilidade'].widget.attrs['placeholder'] = 'Viabilidade'
        self.fields['Situacao'].widget.attrs['placeholder'] = 'Situação'
        self.fields['Data'].widget.attrs['placeholder'] = 'Data'

