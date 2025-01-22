from django.db import models
from django.core.validators import MaxLengthValidator, FileExtensionValidator

class ContentItem(models.Model):
    title = models.CharField(
        max_length=30,
        validators=[MaxLengthValidator(30)],
        verbose_name="Title",
    )
    body = models.TextField(
        validators=[MaxLengthValidator(300)],
        verbose_name="Body",
    )
    summary = models.CharField(
        max_length=60,
        validators=[MaxLengthValidator(60)],
        verbose_name="Summary",
    )
    document = models.FileField(
        upload_to='documents/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['pdf'], message="Only PDF files are allowed."
            ),
        ],
        verbose_name="Document",
    )
    author = models.ForeignKey(
        'authentication.User', on_delete=models.CASCADE, related_name="content_items", verbose_name="Author"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.title
