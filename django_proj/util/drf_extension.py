from rest_framework import serializers, fields
# import six
from collections import OrderedDict


class ChoiceDisplayField(fields.ChoiceField):
    def __init__(self, *args, **kwargs):
        choices = kwargs['choices']
        self._choices = OrderedDict(choices)
        super().__init__(*args, **kwargs)
        # self.choice_strings_to_display = {
        #     six.text_type(key): value for key, value in self.choices.items()
        # }

    def to_representation(self, value):
        if value is None:
            return value
        return {
            # 'key': self.choice_strings_to_values.get(six.text_type(value), value),
            # 'display_name': self.choice_strings_to_display.get(six.text_type(value), value),
            'key': value,
            'display_name': self._choices[value],
        }


class PrimaryKeyWihName(serializers.PrimaryKeyRelatedField):
    # def to_representation(self, value):
    #     if value is None:
    #         return value
    #     return {
    #         'id': value,
    #         'name': value,
    #     }
    def to_representation(self, value):
        if self.pk_field is not None:
            return self.pk_field.to_representation(value.pk)
        return 'value.pk'


class DefaultModelSerializer(serializers.ModelSerializer):
    serializer_choice_field = ChoiceDisplayField

