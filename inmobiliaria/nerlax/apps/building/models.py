from django.db import models
from django.utils.datetime_safe import datetime
from django.contrib.auth import get_user_model
from ..settings.models import *
from ..users.models import UserModel

Users = get_user_model()


class Amenities(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=225, blank=True, null=True)
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Building(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=225, blank=True, null=True)
    address = models.CharField(max_length=225, blank=True, null=True)
    address2 = models.CharField(max_length=225, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.DecimalField(max_digits=5, decimal_places=0,
                                      blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    unit_qty = models.DecimalField(max_digits=2, decimal_places=0)
    amenities = models.BooleanField(blank=True, null=True)
    type_resource = models.ForeignKey(Classification, blank=True, null=True,
                                      on_delete=models.CASCADE)
    supplier = models.ManyToManyField(Supplier, related_name='suppliers',
                                      blank=True, null=True)
    state = models.BooleanField(default=True)
    create_to = models.DateTimeField(auto_now_add=True)
    update_to = models.DateTimeField(auto_now=True)

    create_by = models.ForeignKey(Users, blank=True, null=True, related_name='author_post', on_delete=models.CASCADE)
    update_by = models.ForeignKey(Users, blank=True, null=True, related_name='post_update', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Building'
        verbose_name_plural = 'Buildings'
        ordering = ['create_to']

    def __str__(self):
        return self.name


class Unit(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    number = models.DecimalField(max_digits=2, decimal_places=0)
    meter_qty = models.DecimalField(max_digits=2, decimal_places=0, blank=True,
                                    null=True)
    flat = models.CharField(max_length=20, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    init_date = models.DateField(blank=True, null=True)
    renovation_date = models.DateField(blank=True, null=True)
    rent_price = models.IntegerField(default=0)
    renter = models.ForeignKey(Users, blank=True, null=True,
                               on_delete=models.CASCADE)
    description = models.CharField(max_length=225, blank=True, null=True)
    type_resource = models.ForeignKey(Classification, blank=True, null=True,
                                      on_delete=models.CASCADE)
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
    state = models.BooleanField(default=True)

    create_to = models.DateTimeField(auto_now_add=True)
    update_to = models.DateTimeField(auto_now=True)
    
    # create_by = models.ForeignKey(Users, blank=True, null=True, related_name='author_post', on_delete=models.CASCADE)
    # update_by = models.ForeignKey(Users, blank=True, null=True, related_name='post_update', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'
        ordering = ['create_to']

    def __str__(self):
        return self.name


class CommonExpenses(models.Model):
    id = models.AutoField(primary_key=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    payment_date = models.DateField()
    total_amount = models.IntegerField(default=0)
    state = models.BooleanField(default=True)
    create_to = models.DateTimeField(auto_now_add=True)
    update_to = models.DateTimeField(auto_now=True)

    # create_by = models.ForeignKey(Users, blank=True, null=True, related_name='author_post', on_delete=models.CASCADE)
    # update_by = models.ForeignKey(Users, blank=True, null=True, related_name='post_update', on_delete=models.CASCADE)

    def __str__(self):

        return f'{self.building},{self.payment_date}'

    class Meta:
        verbose_name_plural = 'Common Expenses'
        ordering = ['payment_date']


class CommonExpensesLines(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.IntegerField(default=0)
    concept = models.CharField(max_length=225)
    common_expenses = models.ForeignKey(CommonExpenses, on_delete=models.CASCADE)
    state = models.BooleanField(default=True)
    create_to = models.DateTimeField(auto_now_add=True)
    update_to = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Common Expenses Lines'
        ordering = ['create_to']
