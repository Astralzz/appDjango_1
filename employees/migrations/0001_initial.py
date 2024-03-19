# Generated by Django 5.0.2 on 2024-03-19 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentsReceived',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('hour', models.TimeField()),
                ('date_time_create', models.DateTimeField(auto_now_add=True)),
                ('date_time_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PositionEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(max_length=1000, null=True)),
                ('date_time_create', models.DateTimeField(auto_now_add=True)),
                ('date_time_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noEmployee', models.CharField(db_index=True, max_length=8, unique=True)),
                ('name', models.CharField(max_length=120, unique=True)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('gender', models.CharField(choices=[('F', 'FEMENINO'), ('M', 'MASCULINO'), ('N', 'SIN ESPECIFICAR')], default='N', max_length=1)),
                ('active', models.BooleanField(default=True)),
                ('date_time_create', models.DateTimeField(auto_now_add=True)),
                ('date_time_update', models.DateTimeField(auto_now=True)),
                ('payments', models.ManyToManyField(related_name='payments', to='employees.paymentsreceived')),
            ],
        ),
    ]
