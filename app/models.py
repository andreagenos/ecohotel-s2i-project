from django.db import models
from django.utils import timezone
from .utils import sendTransaction
import hashlib
from django.conf import settings

class Panel(models.Model):
    produced_energy = models.IntegerField(null=True)
    consumed_energy = models.IntegerField(null=True)
    date = models.DateTimeField(default=timezone.now)
    hash = models.CharField(max_length=64, default=None, null=True, blank=True)
    txId = models.CharField(max_length=66, default=None, null=True, blank=True)


    def publish(self):
        self.save()
    
    def __str__(self):
        return self.date.strftime("%Y-%m-%d")
    
    def writeOnChain(self):
        energy_total = str(self.produced_energy)+"-"+str(self.consumed_energy)
        self.hash = hashlib.sha256(energy_total.encode("utf-8")).hexdigest()
        self.txId = sendTransaction(self.hash)
        self.save()
        