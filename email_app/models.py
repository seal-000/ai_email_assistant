# models.py
from django.db import models

class RephrasedText(models.Model):
    user_email = models.EmailField()
    original_text = models.TextField()
    rephrased_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_email} - {self.created_at}"