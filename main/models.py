from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField


# Create your models here.


class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'

    name = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField( blank=True, null=True)
    image = models.ImageField(upload_to='skills', blank=True, null=True)
    is_key_skill = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar', blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to='cv')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    

class ContactProfile(models.Model):
    class Meta:
        ordering = ['timestamp']

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name='Name', max_length=100)
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Message')

    def __str__(self):
        return self.name
    

class Portfolio(models.Model):
    class Meta:
        ordering = ['name']

    date = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    body = HTMLField(blank=True, null=True)
    image = models.ImageField(upload_to='portfolio', null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/portfolio/{self.slug}'


class Media(models.Model):
    class Meta:
        ordering = ['name']

    image = models.ImageField(upload_to='media', null=True, blank=True)
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)
    is_logo = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name