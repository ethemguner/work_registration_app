from django.db import models

class Registry(models.Model):
    STATUS = (
        ('0','Not Confirmed.'),
        ('1','Confirmed.')
    )

    content = models.TextField(blank=False, null=True, max_length=2000)
    entryTime = models.DateTimeField(auto_now_add=True, auto_now=False)
    status = models.CharField(blank=False, null=True, max_length=15,
                              choices=STATUS, editable=False, default='0')

    class Meta:
        verbose_name_plural = 'TODOs'
        ordering = ['entryTime']

    def __str__(self):
        return "TODO - {} | {}".format(self.pk, self.entryTime)