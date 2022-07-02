from django import forms


class HelloAnswer(forms.Form):
    ans = forms.CharField(label='strings', widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    data = [('one', 'xss'), ('two', 'sqli'), ('three', 'oscmmand')]

    choice = forms.ChoiceField(label='Choice', choices=data)


'''
class InputForm(forms.Form):
    strings = forms.CharField(label='name', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))

'''
