from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.

class TrainingClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="training_classes")
    icon = models.FileField(upload_to="training_classes/icons", validators=[FileExtensionValidator(['svg', 'png'])])
    # icon = models.ImageField(upload_to="training_classes/icons")
    fullness = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="posts")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} ||| {self.created_at}'

    class Meta:
        ordering = ['-created_at']

