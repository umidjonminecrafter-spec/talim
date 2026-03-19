from .models import Organizations,Subscriptions,Branch,OrganizationSettings,ExamSettings,Tag
from rest_framework import serializers
from .models import LandingPage, LandingPageSubmission
from datetime import datetime, timedelta



class OrganizationSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationSettings
        fields = '__all__'
        read_only_fields = ('organization', 'created_at', 'updated_at')


class OrganizationSerializer(serializers.ModelSerializer):
    settings = OrganizationSettingsSerializer(read_only=True)

    class Meta:
        model = Organizations
        fields = ['id', 'name', 'logo', 'address', 'phone', 'status', 'created_at', 'settings']
        read_only_fields = ('created_at',)


class OrganizationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizations
        fields = ['name', 'logo', 'address', 'phone', 'status']

    def create(self, validated_data):
        organization = Organizations.objects.create(**validated_data)
        # Avtomatik sozlamalar yaratish (default qiymatlar bilan)
        OrganizationSettings.objects.create(organization=organization)
        return organization


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = '__all__'
        read_only_fields = ('created_at',)


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'
        read_only_fields = ('created_at',)

class ExamSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamSettings
        fields = '__all__'
        read_only_fields = ('organization', 'created_at', 'updated_at')





class LandingPageSerializer(serializers.ModelSerializer):
    submissions_count = serializers.SerializerMethodField()
    full_url = serializers.SerializerMethodField()

    class Meta:
        model = LandingPage
        fields = [
            'id', 'organization', 'name', 'slug', 'branch', 'section',
            'source', 'is_active', 'submissions_count', 'full_url',
            'created_at', 'updated_at'
        ]
        read_only_fields = ('organization', 'created_at', 'updated_at')

    def get_submissions_count(self, obj):
        return obj.submissions.count()

    def get_full_url(self, obj):
        # Misol: https://yourcenter.modme.uz/ielts-kursi
        return f"https://yourcenter.modme.uz/{obj.slug}"


class LandingPageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandingPage
        fields = ['name', 'slug', 'branch', 'section', 'source', 'is_active']

    def validate_slug(self, value):
        # Slug unikal ekanligini tekshirish
        if LandingPage.objects.filter(slug=value).exists():
            raise serializers.ValidationError("Bu slug allaqachon mavjud.")
        return value


class LandingPageSubmissionSerializer(serializers.ModelSerializer):
    landing_page_name = serializers.CharField(source='landing_page.name', read_only=True)

    class Meta:
        model = LandingPageSubmission
        fields = [
            'id', 'landing_page', 'landing_page_name', 'full_name',
            'phone', 'comment', 'branch', 'source', 'created_at'
        ]
        read_only_fields = ('branch', 'source', 'created_at')


class LandingPageSubmissionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandingPageSubmission
        fields = ['landing_page', 'full_name', 'phone', 'comment']


class BillingSubscriptionSerializer(serializers.ModelSerializer):
    days_remaining = serializers.SerializerMethodField()
    is_expiring_soon = serializers.SerializerMethodField()
    organization_name = serializers.CharField(source='organization_id.name', read_only=True)

    class Meta:
        model = Subscriptions
        fields = [
            'id', 'organization_id', 'organization_name', 'plan_type',
            'start_date', 'end_date', 'status', 'price',
            'days_remaining', 'is_expiring_soon', 'created_at'
        ]
        read_only_fields = ('created_at',)

    def get_days_remaining(self, obj):
        """Qolgan kunlar"""
        if obj.end_date:
            delta = obj.end_date.date() - datetime.now().date()
            return delta.days if delta.days > 0 else 0
        return 0

    def get_is_expiring_soon(self, obj):
        """Muddat tugashiga yaqinmi (7 kun ichida)"""
        days = self.get_days_remaining(obj)
        return 0 < days <= 7


class BillingCreateSerializer(serializers.ModelSerializer):
    duration_months = serializers.IntegerField(write_only=True, help_text="Muddat (oyda): 1, 3, 6, 12")

    class Meta:
        model = Subscriptions
        fields = ['plan_type', 'price', 'duration_months']

    def validate_duration_months(self, value):
        if value not in [1, 3, 6, 12]:
            raise serializers.ValidationError("Faqat 1, 3, 6, yoki 12 oy mumkin")
        return value

    def create(self, validated_data):
        duration = validated_data.pop('duration_months')
        start_date = datetime.now()
        end_date = start_date + timedelta(days=30 * duration)

        subscription = Subscriptions.objects.create(
            start_date=start_date,
            end_date=end_date,
            status='active',
            **validated_data
        )
        return subscription


class BillingStatsSerializer(serializers.Serializer):
    """Billing statistikasi"""
    current_subscription = BillingSubscriptionSerializer()
    total_subscriptions = serializers.IntegerField()
    total_spent = serializers.IntegerField()
    next_payment_date = serializers.DateTimeField()
    days_remaining = serializers.IntegerField()
    status = serializers.CharField()




class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", "object_type"]
