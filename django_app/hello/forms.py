from django import forms


class HelloForm(forms.Form):
    name = forms.CharField(label='name', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    mail = forms.CharField(label='mail', widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    other = forms.CharField(label='other', widget=forms.TextInput(
        attrs={'class': 'form-control'}))


class HelloAnswer(forms.Form):
    ans = forms.CharField(label='strings', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
