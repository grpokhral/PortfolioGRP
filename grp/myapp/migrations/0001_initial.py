# Generated by Django 2.2.5 on 2021-02-12 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.IntegerField()),
                ('project', models.IntegerField()),
                ('design', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_title', models.CharField(max_length=100)),
                ('portfolio_subtitle', models.CharField(max_length=100)),
                ('portfolio_image', models.ImageField(upload_to='pics')),
                ('portfolio_detail', models.TextField(max_length=500)),
                ('featured', models.BooleanField()),
                ('portfolio_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Category')),
            ],
        ),
    ]