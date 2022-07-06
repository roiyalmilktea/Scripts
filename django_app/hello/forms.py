from django import forms


class HelloAnswer(forms.Form):
    ans = forms.CharField(label='strings', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    strings = forms.CharField(label='name', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    email = forms.CharField(label='mail', widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    data = [('one', 'xss'), ('two', 'sqli'), ('three', 'oscmmand')]

    choice = forms.ChoiceField(label='Choice', choices=data)


class HelloSearch(forms.Form):
    id = forms.IntegerField(label='ID')
