# Generated by Django 5.0.1 on 2024-01-19 14:56
import django
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('sessions', '0001_initial'),

    ]

    operations = [

        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False,
                                                     help_text='Designates that this user has all permissions without explicitly assigning them.',
                                                     verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('fullname', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('password2', models.CharField(blank=True, max_length=128, null=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='customuser_set', to='auth.group',
                                                  verbose_name='groups')),
                ('user_permissions',
                 models.ManyToManyField(blank=True, related_name='customuser_set', to='auth.permission',
                                        verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),

        migrations.CreateModel(
            name='TrainingClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='training_classes')),
                ('icon', models.ImageField(upload_to='training_classes')),
            ],
        ),

        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='posts')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='trainingclass',
            name='fullness',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='trainingclass',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='trainingclass',
            name='icon',
            field=models.FileField(upload_to='training_classes/icons',
                                   validators=[django.core.validators.FileExtensionValidator(['svg', 'png'])]),
        ),
    ]