from django.db import models

class spex(models.Model):
    spex_name = models.CharField(max_length=30)
    spex_id = models.IntegerField()

    def __str__(self):
        return self.spex_name
class dox(models.Model):
    dox_name = models.CharField(max_length=30)
    dox_spex = models.ForeignKey('spex', on_delete=models.CASCADE)

    def __str__(self):
        return self.dox_name
