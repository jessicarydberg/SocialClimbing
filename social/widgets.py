from django import forms


class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime-local'
    input_formats = ["%d"]