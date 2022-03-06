from django.db import models

# Create your models here.

class CapturedPackets(models.Model):
    p_content = models.TextField(verbose_name="captured_packets")
