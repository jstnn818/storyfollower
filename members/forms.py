from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string

class PrependTextInput(forms.TextInput):
    def __init__(self, prepend='', *args, **kwargs):
        self.prepend = prepend
        super(PrependTextInput, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None, renderer=None):
        input_field = super().render(name, value, attrs, renderer)
        return render_to_string('widgets/prepend_input.html', {'prepend': self.prepend, 'input_field': input_field})

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', "password1", "password2")
        
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs) 
        widgets = {
            'username': ('Enter Username', 'text', '👤'),
            'password1': ('Enter Password', 'password', '🔒'),
            'password2': ('Re-enter Password', 'password', '🔐'),
        }
        
        for fieldname in widgets.keys():
            self.fields[fieldname].widget = PrependTextInput(
                attrs={
                    'placeholder': widgets[fieldname][0], 
                    'type': widgets[fieldname][1], 
                    'class': 'form-control'}, 
                prepend=widgets[fieldname][2])
            self.fields[fieldname].help_text = None