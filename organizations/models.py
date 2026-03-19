from django.db import models
from core.validators import uz_phone_validator
import uuid
from django.utils.text import slugify

from core.models import BaseModel


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


class OrganizationSettings(models.Model):
    # OneToOne relationship
    organization = models.OneToOneField(
        Organizations,
        on_delete=models.CASCADE,
        related_name="settings",
        primary_key=True
    )

    # To'lov rejimi
    PAYMENT_MODE_CHOICES = (
        ("monthly", "Oylik (kalendar oyiga)"),
        ("per_lesson", "Darslik"),
        ("package", "Paket"),
    )
    payment_mode = models.CharField(
        max_length=20,
        choices=PAYMENT_MODE_CHOICES,
        default="monthly"
    )

    # Ish haqi sozlamalari (Salary Settings)
    exclude_trial_students = models.BooleanField(default=True, help_text="Sinov darsidagi talabalarni hisobga olmang")
    exclude_archived_students = models.BooleanField(default=True, help_text="Arxivlangan talabalarni hisobga olmang")
    include_student_discount = models.BooleanField(default=False, help_text="Talaba chegirmasini hisobga oling")
    apply_discount_to_salary = models.BooleanField(default=False,
                                                   help_text="O'qituvchining maoshida o'quvchi chegirmasini hisobga oling")
    calculate_archived_salary = models.BooleanField(default=False,
                                                    help_text="Arxivlangan o'quvchilarga maosh hisoblang")
    link_salary_to_attendance = models.BooleanField(default=True, help_text="O'qituvchining maoshini davomatga ulang")

    # Davomat asosidagi nazorat
    only_main_teacher_attendance = models.BooleanField(default=False,
                                                       help_text="Faqatgina guruh ustozi belgilagan davomatlarga maosh hisoblash")
    only_attended_lessons = models.BooleanField(default=True,
                                                help_text="Faqatgina o'quvchi kelgan darslarga maosh hisoblash")
    calculate_trial_salary = models.BooleanField(default=False,
                                                 help_text="Sinov darsi holatidagi o'quvchilar uchun maosh hisoblash")
    include_frozen_students = models.BooleanField(default=False, help_text="Muzlatilgan o'quvchilarni hisobga olish")

    # Qo'shimcha ruxsatlar (Others)
    allow_teacher_sms = models.BooleanField(default=False, help_text="O'qituvchilarga SMS yuborishga ruxsat bering")
    hide_student_data_from_teacher = models.BooleanField(default=False,
                                                         help_text="O'qituvchilarga talabalar ma'lumotlarini yashirish")
    attendance_only_during_lesson = models.BooleanField(default=False,
                                                        help_text="Davomatni faqat dars davomida belgilash")
    allow_schedule_overlap = models.BooleanField(default=False,
                                                 help_text="Jadval: guruhlarni bitta kabinet/o'qituvchi bilan kesib o'tishga ruxsat")
    show_group_balance = models.BooleanField(default=True, help_text="Guruh balansini ko'rsatish")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "organization_settings"
        verbose_name = "Organization Setting"
        verbose_name_plural = "Organization Settings"

    def __str__(self):
        return f"Settings for {self.organization.name}"





class ExamSettings(models.Model):
    # OneToOne relationship
    organization = models.OneToOneField(
        Organizations,
        on_delete=models.CASCADE,
        related_name="exam_settings",
        primary_key=True
    )

    # Imtihonda hisobga olish sozlamalari
    include_active_students = models.BooleanField(
        default=True,
        help_text="Faol talabalarni hisobga olish"
    )
    include_trial_students = models.BooleanField(
        default=False,
        help_text="Sinov darsidagi talabalarni hisobga olish"
    )
    include_archived_students = models.BooleanField(
        default=False,
        help_text="Arxivlangan talabalarni hisobga olish"
    )
    include_frozen_students = models.BooleanField(
        default=False,
        help_text="Muzlatilgan talabalarni hisobga olish"
    )
    include_deleted_students = models.BooleanField(
        default=False,
        help_text="O'chirilgan talabalarni hisobga olish"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "exam_settings"
        verbose_name = "Exam Setting"
        verbose_name_plural = "Exam Settings"

    def __str__(self):
        return f"Exam Settings for {self.organization.name}"
class Section(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True, null=True, help_text="Qo‘shimcha ma’lumot")
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "sections"
        verbose_name = "Section"
        verbose_name_plural = "Sections"
        ordering = ['name']




class LandingPage(models.Model):
    SOURCE_CHOICES = (
        ("telegram", "Telegram"),
        ("instagram", "Instagram"),
        ("facebook", "Facebook"),
        ("website", "Website"),
        ("offline", "Offline"),
        ("youtube", "YouTube"),
        ("tiktok", "TikTok"),
        ("other", "Boshqa"),
    )

    organization = models.ForeignKey(
        Organizations,
        on_delete=models.CASCADE,
        related_name="landing_pages"
    )
    name = models.CharField(max_length=250, help_text="Landing sahifa nomi")
    slug = models.SlugField(max_length=250, unique=True, help_text="URL qismi")
    branch = models.ForeignKey(
        Branch,
        on_delete=models.SET_NULL,
        null=True,
        related_name="landing_branch",
        help_text="Qaysi filialga biriktiriladi"
    )
    section = models.ForeignKey(
        'Section',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="landing_section",
        help_text="Qaysi kurs/yo'nalish"
    )
    source = models.CharField(
        max_length=20,
        choices=SOURCE_CHOICES,
        help_text="Qaysi platformadan"
    )
    is_active = models.BooleanField(default=True, help_text="Faolmi")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "landing_pages"
        verbose_name = "Landing Page"
        verbose_name_plural = "Landing Pages"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.slug})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class LandingPageSubmission(models.Model):
    landing_page = models.ForeignKey(
        LandingPage,
        on_delete=models.CASCADE,
        related_name="submissions"
    )
    full_name = models.CharField(max_length=250, help_text="To'liq ismi")
    phone = models.CharField(
        max_length=20,
        validators=[uz_phone_validator],
        help_text="Telefon raqam"
    )
    comment = models.TextField(null=True, blank=True, help_text="Qo'shimcha izoh")

    # Avtomatik to'ldiriladi
    branch = models.ForeignKey(
        Branch,
        on_delete=models.SET_NULL,
        null=True,
        related_name="submission_branch"
    )
    source = models.CharField(max_length=20, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "landing_page_submissions"
        verbose_name = "Landing Page Submission"
        verbose_name_plural = "Landing Page Submissions"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.landing_page.name}"

    def save(self, *args, **kwargs):
        # Avtomatik branch va source ni landing page dan olish
        if not self.branch and self.landing_page.branch:
            self.branch = self.landing_page.branch
        if not self.source:
            self.source = self.landing_page.source
        super().save(*args, **kwargs)

class Tag(BaseModel):
    OBJECT_TYPE = (
        ("student", "Student"),
        ("group", "Group"),
        ("lead", "Lead"),
    )

    name = models.CharField(max_length=100)
    object_type = models.CharField(max_length=20, choices=OBJECT_TYPE)

    def __str__(self):
        return f"{self.name} ({self.object_type})"





