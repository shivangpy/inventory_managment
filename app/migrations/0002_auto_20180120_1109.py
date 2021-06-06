# Generated by Django 2.0 on 2018-01-20 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('sub_total', models.FloatField(max_length=100)),
                ('vat', models.FloatField(max_length=100)),
                ('total_amount', models.FloatField(max_length=100)),
                ('discount', models.FloatField(max_length=100)),
                ('grand_total', models.FloatField(max_length=100)),
                ('paid', models.FloatField(max_length=100)),
                ('due', models.FloatField(max_length=100)),
                ('payment_type', models.CharField(max_length=100)),
                ('payment_status', models.IntegerField(max_length=100)),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(max_length=100)),
                ('rate', models.FloatField(max_length=100)),
                ('total', models.FloatField(max_length=100)),
                ('status', models.IntegerField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='media/product/images/')),
                ('quantity', models.IntegerField(max_length=100)),
                ('rate', models.FloatField(max_length=100)),
                ('is_active', models.IntegerField()),
                ('status', models.IntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category')),
            ],
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Product'),
        ),
    ]
