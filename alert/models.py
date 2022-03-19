from django.db import models

# Create your models here.

class CapturedPackets(models.Model):
    title = models.TextField(verbose_name="title")
    p_content = models.TextField(verbose_name="captured_packets")


    def __str__(self):
        return self.title
    