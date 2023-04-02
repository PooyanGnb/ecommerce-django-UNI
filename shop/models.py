from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120)
    category = models.ManyToManyField(Category)
    color = models.ManyToManyField(Color)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField()
    status = models.BooleanField(default=False)
    counted_views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f' {self.name} - {self.id} '

    def view_increament(self):
        self.counted_views += 1
        self.save()

    def get_absolute_url(self):
        return reverse('shop:detail', kwargs={'slug': self.slug})
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return f' {self.product.name}'


class Size(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f' {self.product.name} - {self.size} '

    def decreament(self):
        self.quantity -= 1
        self.save()


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class NewsLetter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email