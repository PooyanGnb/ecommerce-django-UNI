from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    @property
    def numcount(self):
        return Product.objects.filter(color=self.id).count()
    

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

    class Meta:
        ordering = ['size']

    def __str__(self):
        return f' {self.product.name} - {self.size} '

    def decreament(self):
        self.quantity -= 1
        self.save()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.id}'
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        return sum([item.get_total for item in orderitems])
    
    @property
    def get_cart_item(self):
        orderitems = self.orderitem_set.all()
        return sum([item.quantity for item in orderitems])
    

class OrderItem(models.Model):
    product =  models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity =  models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        return self.product.price * self.quantity


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
    

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f' {self.name} - {self.product} '