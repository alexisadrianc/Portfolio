from django.db import models
from django.db.models.signals import post_save

# Create your models here.


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    rut_dgi = models.CharField(max_length=100)
    address = models.CharField(max_length=225, blank=True, null=True)
    address2 = models.CharField(max_length=225, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    state = models.BooleanField(default=True)
    create_to = models.DateTimeField(auto_now_add=True)
    update_to = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class Classification(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=225, blank=True, null=True)
    state = models.BooleanField(default=True)
    create_to = models.DateTimeField(auto_now_add=True)
    update_to = models.DateTimeField(auto_now=True)
    # create_by = models.ForeignKey(Users, blank=True, null=True, related_name='author_post', on_delete=models.CASCADE)
    # update_by = models.ForeignKey(Users, blank=True, null=True, related_name='post_update', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Classification'
        verbose_name_plural = 'Classifications'
        ordering = ['create_to']

    def __str__(self):
        return self.name


class ActivityType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True, null=True)
    state = models.BooleanField(default=True)
    create_to = models.DateTimeField(auto_now_add=True)
    update_to = models.DateTimeField(auto_now=True)
    # create_by = models.ForeignKey(Users, blank=True, null=True, related_name='author_post', on_delete=models.CASCADE)
    # update_by = models.ForeignKey(Users, blank=True, null=True, related_name='post_update', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Activity type'
        verbose_name_plural = 'Activity types'
        ordering = ['create_to']

    def __str__(self):
        return self.name


class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=225, blank=True, null=True)
    address2 = models.CharField(max_length=225, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    nro_documento = models.CharField(max_length=15)
    logo = models.ImageField(blank=True, null=True, default="images/logoner.png", upload_to="images/")
    state = models.BooleanField(default=True)
    create_to = models.DateTimeField(auto_now_add=True)
    update_to = models.DateTimeField(auto_now=True)
    # create_by = models.ForeignKey(UserModel, blank=True, null=True, related_name='author_post', on_delete=models.CASCADE)
    # update_by = models.ForeignKey(UserModel, blank=True, null=True, related_name='post_update', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
        ordering = ['create_to']

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name)


class Services(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    supplier = models.ForeignKey(Supplier, blank=True, null=True, on_delete=models.CASCADE)
    state = models.BooleanField(default=True)
    create_to = models.DateTimeField(auto_now_add=True)
    update_to = models.DateTimeField(auto_now=True)

    # create_by = models.ForeignKey(Users, blank=True, null=True, related_name='author_post', on_delete=models.CASCADE)
    # update_by = models.ForeignKey(Users, blank=True, null=True, related_name='post_update', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['create_to']

    def __str__(self):
       return self.name

    def natural_key(self):
        return (self.name)


def remove_ralational_supplier(sender, instance, **kwargs):
    if instance.state == False:
        supplier = instance.id
        services = Services.objects.filter(supplier=supplier)
        for rec in services:
            rec.supplier.remove(supplier)
post_save.connect(remove_ralational_supplier, sender=Supplier)


class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=3, blank=True, null=True)
    active = models.BooleanField(default=True)
    create_to = models.DateTimeField(auto_now_add=True)
    update_to = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'States'
        ordering = ['name']

    def __str__(self):
       return self.name

    def natural_key(self):
        return (self.name)


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    create_to = models.DateTimeField(auto_now_add=True)
    update_to = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ['name']

    def __str__(self):
       return self.name

    def natural_key(self):
        return (self.name)


def remove_ralational_state(sender, instance, **kwargs):
    if instance.active == False:
        state = instance.id
        city = State.objects.filter(state=state)
        for rec in city:
            rec.state.remove(state)
post_save.connect(remove_ralational_state, sender=State)


