from rest_framework import serializers
from .models import Organizations,Subscriptions,Branch

class OrganizationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizations
        fields = "__all__"


class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = "__all__"


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"