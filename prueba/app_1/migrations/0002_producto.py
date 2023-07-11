# Generated by Django 4.2.3 on 2023-07-11 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcionProducto', models.TextField(default='Sin descripcion')),
                ('stockProducto', models.IntegerField()),
                ('precioProducto', models.IntegerField()),
                ('imagProducto', models.ImageField(default='medios/not-found.jpg', upload_to='medios')),
            ],
        ),
    ]