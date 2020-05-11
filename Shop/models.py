from django.db import models
# Create your models here.
class Product(models.Model):   
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_catagory = models.CharField(max_length=50)
    product_subcatagory = models.CharField(max_length=50,default='')
    product_desc = models.CharField(max_length=300)
    product_pricse = models.IntegerField(default=0)
    product_pub_date = models.DateField()
    product_imag = models.ImageField(upload_to='shope/images')

    def __str__(self):
        return self.product_name

class Contact_us(models.Model):
    contacter_name = models.CharField(max_length=30)
    contacter_mail = models.CharField(max_length=30)
    contacter_phone = models.CharField(max_length=13)
    contacter_desc = models.CharField(max_length=500)

    def __str__(self):
        return self.contacter_name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")
        
    def __str__(self):
        return str(self.order_id)
    
class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."

class OrderUpdated(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."

