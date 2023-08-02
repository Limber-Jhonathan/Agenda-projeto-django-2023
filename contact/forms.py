from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth import password_validation

from . import models
#campo contact/create/
class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe_a',
                'placeholder': 'Digite o primeiro nome',
            }
        ),
        label= 'Primeiro nome',
        help_text= "Texto de ajuda para o usuario",
    )
    class Meta:
        model = models.Contact
        fields = 'first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture',
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

class RegisterForm(UserCreationForm):
    #campo obrigadorio com minimo de 3 caracteres
    first_name = forms.CharField(
    required=True,
    min_length=3,
    error_messages={
        'requerid':'Campo obrigatorio'
    }
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
    )
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 'password1', 'password2',
        )

    #verifiação de email existente
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Este email já existe', code='invalid')
            )
        return email

class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.',
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.'
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use the same password as before.',
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )
    
    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)

        password = cleaned_data.get('password1')
        
        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError("Senhas não batem")
                )


    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Este email já existe', code='invalid')
                )
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        
        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as error:
                self.add_error(
                    'password1',
                    ValidationError(error)
                )
        return password1