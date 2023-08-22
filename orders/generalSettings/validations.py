from django.core.exceptions import ValidationError
import re
from django import forms
from pos_project import constants

def validate_24_hours_format(value):
    if not re.match(r'^([0-9]{2}):([0-9]{2})$', value):
        raise ValidationError('Time must be in 24 hours format')

def validate_hour(value):
    if int(value) > 24:
        raise ValidationError("Hour can't be greater than 24")

def validate_minute(value):
    if int(value) > 59:
        raise ValidationError("Minute can't be greater than 59")

class TimingValidator:
    def __call__(self, value):
        validate_24_hours_format(value['from'])
        validate_24_hours_format(value['to'])
        validate_hour(value['from'][:2])
        validate_hour(value['to'][:2])
        validate_minute(value['from'][3:])
        validate_minute(value['to'][3:])

class StatusValidator:
    def __call__(self, value):
        if not isinstance(value, dict):
            raise ValidationError('Invalid value type')
        if 'web' not in value or 'app' not in value:
            raise ValidationError('Missing web or app status')
        if not isinstance(value['web'], dict) or not isinstance(value['app'], dict):
            raise ValidationError('Invalid web or app status type')

        web_status = value['web']
        app_status = value['app']

        if 'active' not in web_status or 'message' not in web_status:
            raise ValidationError('Missing web active or message')
        if 'active' not in app_status or 'message' not in app_status:
            raise ValidationError('Missing app active or message')

        if not isinstance(web_status['active'], bool) or not isinstance(app_status['active'], bool):
            raise ValidationError('Invalid active status type')
        if not isinstance(web_status['message'], str) or not isinstance(app_status['message'], str):
            raise ValidationError('Invalid message type')
        if len(web_status['message']) < 10 or len(app_status['message']) < 10:
            raise ValidationError('Message length must be at least 10 characters')


class AdditionalChargesForm(forms.Form):
    brand_id = forms.IntegerField()
    value = {
        'name': forms.CharField(min_length=3),
        'value_type': forms.ChoiceField(choices=constants.ADDITIONAL_CHARGES_KEYS['VALUE_TYPE'].items()),
        'value': forms.DecimalField(min_value=0),
        'type': forms.ChoiceField(choices=constants.ADDITIONAL_CHARGES_KEYS['TYPE'].items()),
        'target': forms.ChoiceField(choices=constants.ADDITIONAL_CHARGES_KEYS['TARGET'].items()),
    }

class AdditionalChargesUpdateForm(forms.Form):
    id = forms.IntegerField()
    value = {
        'name': forms.CharField(min_length=3),
        'value_type': forms.ChoiceField(choices=constants.ADDITIONAL_CHARGES_KEYS['VALUE_TYPE'].items()),
        'value': forms.DecimalField(min_value=0),
        'type': forms.ChoiceField(choices=constants.ADDITIONAL_CHARGES_KEYS['TYPE'].items()),
        'target': forms.ChoiceField(choices=constants.ADDITIONAL_CHARGES_KEYS['TARGET'].items()),
    }


class SettingsGetForm(forms.Form):
    type = forms.ChoiceField(
        choices=[
            (item, item) for item in constants.GENERAL_SETTINGS if item != 'DETECTION_TYPES'
        ]
    )
    count = forms.IntegerField(required=False)
    offset = forms.IntegerField(required=False)
    brand_id = forms.IntegerField(required=False)

class UpdateOutletsForm(forms.Form):
    items = {
        'settings': {
            setting: forms.DecimalField() for setting in constants.GENERAL_SETTINGS if setting != 'DETECTION_TYPES' and setting != 'DELIVERY_DETECTION'
        },
        'outlet_id': forms.IntegerField(min_value=1),
    }

