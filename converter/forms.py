from django import forms
from btndom.helpers.choices import extension_choices


class ConverterForm(forms.Form):
    media = forms.FileField(widget=forms.FileInput(attrs={
                'class':"custom-file-input",'required':'True', 'type':"file", 'accept':"video/*"
                }),required=True
            )
    input_ext = forms.ChoiceField(choices=extension_choices.EXTENSION_CHOICES, label="", initial='Select Extension', 
                widget=forms.Select(attrs={
                'class': 'custom-select d-block w-100',
                }))
    output_ext = forms.ChoiceField(choices=extension_choices.EXTENSION_CHOICES, label="", initial='Select Extension', 
                widget=forms.Select(attrs={
                'class': 'custom-select d-block w-100',
                }))                

class ReconvertForm(forms.Form):
    pk = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'hidden': 'hidden', 'min': 1
        })
    )
    quality_type = forms.ChoiceField(choices=extension_choices.QUALITY_CHOICES, label="Keep or reduce quality", 
                widget=forms.RadioSelect(attrs={        
                }))                
    output_ext = forms.ChoiceField(choices=extension_choices.EXTENSION_CHOICES, label="", initial='Select Extension', 
                widget=forms.Select(attrs={
                'class': 'custom-select w-40',
                'style': 'width: 40%'
                }))