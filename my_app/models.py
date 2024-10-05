from django.db import models
import uuid


class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class News(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    long_description = models.TextField()
    image = models.ImageField(upload_to='news/', null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    view_count = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Партнеры
class Partner(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    website = models.URLField()
    logo = models.ImageField(upload_to='partners/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Публикации
class Publication(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Отзывы
class Review(models.Model):
    service = models.ForeignKey('Service', on_delete=models.CASCADE)  # Добавлено поле для связи с моделью Service
    rating = models.IntegerField(default=3)  # Добавлено поле для рейтинга
    full_name = models.CharField(max_length=50)
    description = models.TextField()
    file = models.FileField(upload_to='reviews/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    guid = models.UUIDField(default=uuid.uuid4, unique=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


# Сервис
class Service(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    view_count = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Член команды
class TeamMember(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    sphere_of_activity = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    scientific_degree = models.CharField(max_length=100, null=True, blank=True)
    legal_practice = models.TextField()
    license = models.CharField(max_length=100, null=True, blank=True)
    membership = models.CharField(max_length=100, null=True, blank=True)
    languages = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_members/', null=True, blank=True)
    slug = models.SlugField(max_length=400, unique=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
