from django.db import models
import datetime

#To generate unique id limiting with 4 char of micro seconds to use for policy and Customer
def genepk():
    cust_id = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')[:-4]
    return cust_id

# Create your models here.
class Customer(models.Model):
    """
    Building unique key using customer login mail with generated key , but keeping character primary has impact with performance when this grow high
    """
    customer_id = models.IntegerField(primary_key=True, default=genepk)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    #full_name = models.CharField(max_length=52)
    dob = models.DateField()
    added = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)


class Policy(models.Model):
    """
    Generating 16 digit unique id , as next step I will merge 4 char of customer id as last i.e
    customer_id : 2021102023525688 then
    quote_id = newkey +  5688

    quote_id = models.IntegerField()

    def save(self, *args, **kwargs):
        self.quote_id = int(f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')[:-4]}{customer_id[-4:]}")
        super(Policy, self).save(*args, **kwargs) # Call the "real" save() method.
    """
    quote_id = models.IntegerField(primary_key=True, default=genepk)
    customer_id = models.IntegerField()
    type = models.CharField(max_length=50)
    premium = models.IntegerField()
    duration = models.IntegerField()
    cover = models.IntegerField()
    state = models.CharField(max_length=10, default='new')
    added = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
