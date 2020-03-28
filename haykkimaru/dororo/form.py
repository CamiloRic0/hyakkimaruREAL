from django import forms
from dororo.models import partesCuerpo, Ubicaciones, Resultados, Demonios, Peleas, articulosDororo


class formularioPartesCuerpo(forms.ModelForm):
    class Meta:
        model = partesCuerpo
        fields = ['nombreParteCuerpo']
        labels = {'nombreParteCuerpo': 'Nombre de la parte del cuerpo'}
        widget = {'nombreParteCuerpo': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control labelForm', 'autocomplete': 'off', 'spellcheck':'false'
            })

class formularioUbicaciones(forms.ModelForm):
    class Meta:
        model = Ubicaciones
        fields = ['nombreUbicacion']
        labels = {'nombreUbicacion': 'Nombre de la ubicacion'}
        widget = {'nombreUbicaciones': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control', 'autocomplete': 'off', 'spellcheck':'false'
            })

class fkPartesCuerpo(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.nombreParteCuerpo)

class fkUbicacion(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.nombreUbicacion)

class fkResultado(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.derrotado)

class formularioDemonios(forms.ModelForm):
    parteCuerpo = fkPartesCuerpo(queryset=partesCuerpo.objects.order_by('id'))
    lugarHogar = fkUbicacion(queryset=Ubicaciones.objects.order_by('id'))
    derrotado = fkResultado(queryset=Resultados.objects.order_by('id'))
    class Meta:
        model = Demonios
        fields = ['nombreDemonio', 'parteCuerpo', 'lugarHogar', 'derrotado', 'fotoDemonio']
        labels = {'nombreDemonio': 'Nombre del demonio'}
        widget = {'nombreDemonio': forms.TextInput(), 'derrotado': forms.ChoiceField(),'fotoDemonio': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control', 'autocomplete': 'off', 'spellcheck':'false'
            })
            self.fields['parteCuerpo'].label = 'Parte del cuerpo'
            self.fields['lugarHogar'].label = 'Lugar del demonio'
            self.fields['derrotado'].label = '¿Fue derrotado el demonio?'

class fkDemonio(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.nombreDemonio)

class formularioPeleas(forms.ModelForm):
    lugarPelea = fkUbicacion(queryset=Ubicaciones.objects.order_by('id'))
    id_Demonio = fkDemonio(queryset=Demonios.objects.order_by('id'))
    ganadorDemonio = fkResultado(queryset=Resultados.objects.order_by('id'))
    class Meta:
        model = Peleas
        fields = ['lugarPelea', 'id_Demonio', 'ganadorDemonio']
        labels = {}
        widget = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
       
class formularioArticulosDororo(forms.ModelForm):
    castigoDororo = fkResultado(queryset=Resultados.objects.order_by('id'))
    class Meta:
        model = articulosDororo
        fields = ['nombreArticulo', 'procedenciaArticulo', 'castigoDororo']
        labels = {'nombreArticulo': 'Nombre del articulo', 'procedenciaArticulo': 'Procedencia del articulo'}
        widget = {'nombreArticulo': forms.TextInput(), 'procedenciaArticulo': forms.TextInput(),}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control', 'autocomplete': 'off', 'spellcheck':'false'
            })
