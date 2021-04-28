from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.


class Base(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.BooleanField(default=True)
    create_to = models.DateTimeField(auto_now_add=True)
    update_to = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        verbose_name = "Base"
        verbose_name_plural = "Bases"


class Teacher(Base):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/teacher/')
    description = models.TextField()
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def __str__(self):
        return self.name


class Lesson(Base):
    name = models.CharField(max_length=254, unique=True)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='images/lesson/')
    slug = models.CharField(max_length=200, unique=True)
    quantity_lesson = models.PositiveIntegerField(default=0)
    description = models.TextField()
    resume = models.TextField()

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"

    def __str__(self):
        return self.name

    def slug(self):
        return slugify(self.name)


class Post(Base):
    name = models.CharField(max_length=50)
    name2 = models.CharField(max_length=50)
    resume = models.TextField()
    slug = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/post')
    published = models.BooleanField(default=False)
    published_date = models.DateField()

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return '{0} {1}'.format(self.name, self.name2)

    def slug(self):
        return slugify('{0} {1}'.format(self.name, self.name2))


class Offer(Base):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/offer')
    resume = models.TextField()
    description = models.TextField()
    period = models.CharField(max_length=200)
    published = models.BooleanField(default=False)
    published_date = models.DateField()

    class Meta:
        verbose_name = "Offer"
        verbose_name_plural = "Offers"

    def __str__(self):
        return self.name


class Testimonial(Base):
    detail = models.TextField()
    image = models.ImageField(upload_to='images/testimonial/')
    author = models.CharField(max_length=200)
    published = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return self.author


class AboutUs(Base):
    company = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/about/')
    about_us = models.TextField()
    name2 = models.CharField(max_length=100, null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=70)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=200)
    title_resume = models.CharField(max_length=200, null=True, blank=True)
    resume = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "AboutUs"
        verbose_name_plural = "AboutsUs"

    def __str__(self):
        return self.name


class Social(Base):
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Socials"

    def __str__(self):
        return self.facebook


class Contact(Base):
    name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.name


class Subscriber(Base):
    email = models.EmailField(max_length=200)

    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"

    def __str__(self):
        return self.email


class ExternalServices(Base):
    name_test = models.CharField(max_length=200)
    test = models.URLField(null=True, blank=True)
    name_theoretical = models.CharField(max_length=200)
    theoretical = models.URLField(null=True, blank=True)
    name_reservation = models.CharField(max_length=200)
    reservation = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = "ExternalService"
        verbose_name_plural = "ExternalServices"

    def __str__(self):
        return self.name_test


class TestRequest(Base):
    TEST = [
        ('teorico', 'Teórico'),
        ('practico', 'Práctico')
    ]

    test_type = models.CharField(max_length=10, choices=TEST)
    name = models.CharField(max_length=200)
    ci = models.CharField(max_length=15)
    trainer = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    time_available = models.CharField(max_length=50)
    qty_lesson = models.PositiveIntegerField(default=0)
    phone = models.CharField(max_length=11)
    email = models.EmailField()

    class Meta:
        verbose_name = "TestRequest"
        verbose_name_plural = "TestsRequest"

    def __str__(self):
        return '{0} - {1}'.format(self.name, self.test_type)
