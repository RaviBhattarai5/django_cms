from django.db import models

class CustomerMaster(models.Model):
    contact_name = models.CharField(max_length=255, verbose_name="Contact Name")
    company_name = models.CharField(max_length=255, verbose_name="Company Name")
    address = models.TextField(verbose_name="Address")
    mobile = models.CharField(max_length=15, verbose_name="Mobile Number")
    email = models.EmailField(max_length=255, unique=True, verbose_name="Email Address")

    def __str__(self):
        return f'{self.contact_name} ({self.company_name})'

    class Meta:
        verbose_name = "Company Contact"
        verbose_name_plural = "Company Contacts"
        ordering = ['company_name']
        db_table = 'CustomerMaster'   
