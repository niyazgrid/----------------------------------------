from django.db import models

class EmailAccount(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Не забывайте о шифровании пароля

class Message(models.Model):
    subject = models.CharField(max_length=255)
    sent_at = models.DateTimeField()
    received_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    attachments = models.FileField(upload_to='attachments/', null=True, blank=True)
    account = models.ForeignKey(EmailAccount, related_name='messages', on_delete=models.CASCADE)

