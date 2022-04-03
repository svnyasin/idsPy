from sqlite3 import Timestamp
from django.db import models

# Create your models here.


class CapturedPacket(models.Model):
    time = models.DateTimeField(verbose_name="time_stamp")
    title = models.TextField(verbose_name="title")
    rule = models.TextField(verbose_name="rule")
    p_content = models.TextField(verbose_name="captured_packets")
    source = models.TextField(verbose_name="source_ip")
    dest = models.TextField(verbose_name="destination_ip")
    s_port = models.TextField(verbose_name="source_port")
    d_port = models.TextField(verbose_name="destination_port")
    protocol = models.TextField(verbose_name="protocol")

    def __str__(self):
        return self.title


class ArchivedPacket(models.Model):
    time = models.DateTimeField(verbose_name="time_stamp")
    title = models.TextField(verbose_name="title")
    rule = models.TextField(verbose_name="rule")
    p_content = models.TextField(verbose_name="captured_packets")
    source = models.TextField(verbose_name="source_ip")
    dest = models.TextField(verbose_name="destination_ip")
    s_port = models.TextField(verbose_name="source_port")
    d_port = models.TextField(verbose_name="destination_port")
    protocol = models.TextField(verbose_name="protocol")

    def __str__(self):
        return self.title
