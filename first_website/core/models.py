from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    thumbnail = models.ImageField(upload_to="products/")
    title = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)

    def rating(self):
        reviews = self.review_set.all()
        if not reviews:
            return 0
        rating = sum([
            review.rating for review in reviews
        ]) / len(reviews)
        return rating



# class Discount(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#     discount = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])


class Review(models.Model):
    class Meta:
        unique_together = ["user", "product"]
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)])
