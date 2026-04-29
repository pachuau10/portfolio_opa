from django.db import models
from ckeditor.fields import RichTextField

class GalleryItem(models.Model):
    CATEGORY_CHOICES = [
        ('film', 'Short Film'),
        ('music', 'Music Video'),
        ('doc', 'Documentary'),
        ('commercial', 'Commercial'),
        ('event', 'Event'),
    ]

    title = models.CharField(max_length=160)
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES, default='film')
    year = models.PositiveIntegerField(default=2025)
    description = RichTextField(blank=True)
    image = models.ImageField(upload_to='gallery/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return f'{self.title} ({self.year})'

    @property
    def display_image(self):
        if self.image:
            return self.image.url
        return ''


class Experience(models.Model):
    role = models.CharField(max_length=160)
    company = models.CharField(max_length=160)
    period = models.CharField(max_length=64, help_text='e.g. 2023 — Present')
    description = RichTextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.role} — {self.company}'


class Skill(models.Model):
    name = models.CharField(max_length=80)
    level = models.PositiveIntegerField(default=80, help_text='0–100')
    icon_url = models.URLField(blank=True, help_text='Logo URL (e.g. simpleicons.org)')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
    

class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.subject or "(no subject)"}'