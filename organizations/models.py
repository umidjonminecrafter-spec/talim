from django.db import models
from core.validators import uz_phone_validator
import uuid

# Yangilangan organization model
class Organizations(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    STATUS = (
        ("active", "Aktiv holatda"),
        ("inactive", "Aktiv emas"),
        ("expires", "To'lov muddati yaqin"),
        ("expired", "To'lov muddati tugagan"),
    )
    name = models.CharField(max_length=250)
    logo = models.FileField(upload_to="org/logos/", null=True, blank=True)
    address = models.TextField()
    phone = models.CharField(max_length=20, validators=[uz_phone_validator,], unique=True)
    status = models.CharField(max_length=20, choices=STATUS)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Subscriptions(models.Model):
    organization_id = models.ForeignKey(Organizations, on_delete=models.CASCADE, related_name="subscriptions_org")
    plan_type = models.CharField(max_length=20)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=20)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plan_type


class Branch(models.Model):
    organization_id = models.ForeignKey(Organizations, on_delete=models.CASCADE, related_name="branch_org")
    name = models.CharField(max_length=250)
    address = models.TextField()
    phone = models.CharField(max_length=20, validators=[uz_phone_validator,], unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)




