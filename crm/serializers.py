from rest_framework import serializers
from .models import (
    CRMSource, CRMPipelines, CRMLead,
    CRMActivity, CRMLeadsHistory,
    CRMLostReason, CRMLeadLost, CRMLeadNotes
)


class CRMSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CRMSource
        fields = "__all__"





class CRMPipelinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CRMPipelines
        fields = "__all__"






class CRMLeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CRMLead
        fields = "__all__"

    def validate_full_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Ism juda qisqa")
        return value





class CRMActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CRMActivity
        fields = "__all__"







class CRMLeadsHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CRMLeadsHistory
        fields = "__all__"






class CRMLostReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CRMLostReason
        fields = "__all__"




class CRMLeadLostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CRMLeadLost
        fields = "__all__"





class CRMLeadNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CRMLeadNotes
        fields = "__all__"
