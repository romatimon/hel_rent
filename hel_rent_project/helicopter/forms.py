from django import forms

from helicopter.models import Helicopter, Applications


class ApplicationForm(forms.ModelForm):
    """Форма заявки."""
    helicopter = forms.ModelChoiceField(queryset=Helicopter.objects.all(),
                                        empty_label="Модель не выбрана",
                                        label="Выбрать модель вертолета")

    class Meta:
        model = Applications
        fields = ['full_name', 'number_phone', 'email', 'helicopter', 'number_of_passengers']
