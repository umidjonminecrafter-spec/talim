from rest_framework import serializers
from .models import SmsTemplates, SmsSchedules, SMSMessages


class SmsTemplatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmsTemplates
        fields = "__all__"

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Nomi kamida 3 ta belgidan iborat bo‘lishi kerak")
        return value


class SmsSchedulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmsSchedules
        fields = "__all__"

    def validate(self, data):
        if not data.get("send_at") and not data.get("cron_expression"):
            raise serializers.ValidationError(
                "send_at yoki cron_expression dan bittasi bo‘lishi kerak"
            )
        return data


class SMSMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSMessages
        fields = "__all__"
