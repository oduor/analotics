from django.db import models

# Create your models here.
class Lots(models.Model):
    name = models.CharField(max_length=200)
    spaces = models.IntegerField()

    class Meta:
        verbose_name = "Lot"
        verbose_name_plural = "Lots"

    def __unicode__(self):
        return str(self.name)

class License(models.Model):
    plate = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "License"
        verbose_name_plural = "Licenses"

    def __unicode__(self):
        return str(self.plate)

class CheckIn(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField()
    license = models.ForeignKey("License")
    lot = models.ForeignKey("Lots")

    class Meta:
        verbose_name = "CheckIn"
        verbose_name_plural = "CheckIns"

    def __unicode__(self):
        return "CheckIn"
