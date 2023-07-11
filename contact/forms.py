from django import forms
from django.core.exceptions import ValidationError
from . import models
#campo contact/create/
class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe_a',
                'placeholder': 'Aqui veio do init',
            }
        ),
        label= 'Primeiro nome',
        help_text= "Texto de ajuda para o usuario",
    )
    class Meta:
        model = models.Contact
        fields = 'first_name', 'last_name', 'phone', 'email', 'description', 'category',
        # widgets = {
        #     # 'first_name': forms.PasswordInput()
        #     # 'first_name':forms.Textarea()
        #     'first_name':forms.TextInput(
        #         attrs={
        #             'class': 'classe_b',
        #             'placeholder':'Escreva aqui'
        #         }
        #     )
        # }

    #Erros lançados /verfificando
    # 2º
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get('last_name')

        msg = ValidationError(
                    "Primeiro nome e o segundo nome não podem ser iguais",
                    code='invalid'
                )

        if first_name == last_name:
            self.add_error('first_name',msg)
            self.add_error('last_name',msg)

        return super().clean()
    
    # 1º
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
            'first_name',
            ValidationError(
                "Veio do add_error",
                code='invalid'
                )
            )
        
        return first_name
