from django.db import models

import Accounts.models as accounts_models

# Create your models here.


class Order(models.Model):
    customer = models.ForeignKey(accounts_models.Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
