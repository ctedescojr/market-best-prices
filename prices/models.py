from django.db import models


class Base(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


class Market(models.Model):
    marketName = models.CharField(max_length=100, verbose_name="Name of the Market")
    city = models.CharField(max_length=100)
    adress = models.CharField(max_length=100, verbose_name="Adress")
    obs = models.TextField(blank=True, null=True, verbose_name="Observation")

    def __str__(self):
        return self.marketName


class Product(Base):
    productName = models.CharField(max_length=100, verbose_name="Name of the Product")
    brand = models.CharField(max_length=100)
    category = models.CharField(
        choices=(
            ("G", "Grains"),
            ("P", "Meat"),
            ("S", "Spices"),
            ("F", "Fruits"),
            ("V", "Vegatables"),
            ("H", "Hygiene"),
            ("C", "Cleaning"),
            ("B", "Beverages"),
            ("D", "Candies"),
        ),
        max_length=1,
    )
    obs = models.TextField(blank=True, null=True, verbose_name="Observation")

    def __str__(self):
        return self.productName


class Price(Base):
    class Meta:
        verbose_name_plural = "Prices"

    id_market = models.ForeignKey(Market, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=6, decimal_places=2)


class Purchases(Base):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_price = models.ForeignKey(Price, on_delete=models.CASCADE)
    purchaseDate = models.DateField(blank=True, null=True)
