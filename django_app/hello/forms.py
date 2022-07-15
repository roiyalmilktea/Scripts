from django import forms


class HelloAnswer(forms.Form):
    strings = forms.CharField(label='strings', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    name = forms.CharField(label='name', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    mail = forms.CharField(label='mail', widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    data = [('xss', 'xss'), ('sqli', 'sqli'), ('oscommandi', 'oscommandi')]

    choice = forms.ChoiceField(label='Choice', choices=data)


class HelloSearch(forms.Form):
    id = forms.IntegerField(label='ID')
