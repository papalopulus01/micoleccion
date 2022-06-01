from django import forms

class Novelas_formularios(forms.Form):

    titulo = forms.CharField(max_length=40)
    autor = forms.CharField(max_length=40)
    editorial = forms.CharField(max_length=40)

class Comics_formularios(forms.Form):
    titulo = forms.CharField(max_length=40)
    numero = forms.FloatField()
    guionista = forms.CharField(max_length=40)
    dibujante = forms.CharField(max_length=40)
    editorial = forms.CharField(max_length=40)

class Mangas_formularios(forms.Form):
    titulo = forms.CharField(max_length=40)
    numero = forms.IntegerField()
    autor = forms.CharField(max_length=40)
    editorial = forms.CharField(max_length=40)


