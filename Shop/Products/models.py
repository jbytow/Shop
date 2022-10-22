from django.db import models

class Producer(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=60)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Producer"
        verbose_name_plural = "Producers"

class Category(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=60)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Products(models.Model):
    def __str__(self):
        return self.name + " "

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=999999999, decimal_places=2)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

