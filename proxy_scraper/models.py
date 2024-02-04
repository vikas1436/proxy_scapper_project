from django.db import models

class Proxy(models.Model):
    ip = models.CharField(max_length=15)
    port = models.CharField(max_length=5)
    protocol = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    uptime = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.ip}:{self.port} - {self.protocol}"