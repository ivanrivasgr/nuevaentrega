from django import forms

class ProductoFormulario(forms.Form):
    nombreCompleto = forms.CharField()
    Referencia = forms.IntegerField()
    fechadecaducidad = forms.DateField()
    categoria = forms.CharField()

class VendedorFormulario(forms.Form):
    nombreCompleto = forms.CharField(max_length=40)
    telefono = forms.IntegerField()
    fechaNac = forms.DateField()

class ClienteFormulario(forms.Form):
    nombreCompleto = forms.CharField(max_length=40)
    telefono = forms.IntegerField()
    fechaNac = forms.DateField()