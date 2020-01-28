from django.db import models


class AbstractNameEntity(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Category(AbstractNameEntity):
    pass


class Brand(AbstractNameEntity):
    pass


class Size(AbstractNameEntity):
    pass


class Image(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url


class Price(models.Model):
    price = models.FloatField(null=True, blank=True)
    currency = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f"{self.price} {self.currency}"


class Product(AbstractNameEntity):
    price = models.OneToOneField(Price, on_delete=models.CASCADE, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    sizes = models.ManyToManyField(Size, related_name='products')
    images = models.ManyToManyField(Image, related_name='products')
    description = models.TextField()
