# Generated by Django 5.0.2 on 2024-02-22 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('added', models.DateField(null=True)),
                ('upadte', models.DateField(null=True)),
            ],
        ),
    ]
