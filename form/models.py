from django.db import models

class Buyer(models.Model):
    buyer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.IntegerField(max_length=10)

class Meta:
    db_table=u'Buyer'

    def __unicode__(self):
        return u"%d %s %s %s %d" % (self.pk, self.first_name, self.last_name, self.email,self.phone)
