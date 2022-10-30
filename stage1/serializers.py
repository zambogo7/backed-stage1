from rest_framework import serializers
from stage1.models import Stage1

class Stage1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Stage1
        fields = (
            'slackUsername',
            'backend',
            'age',
            'bio'
        )