# Generated by Django 3.0.8 on 2020-07-25 12:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dezzex_app', '0002_auto_20200725_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(default='', null=True, upload_to='upload/customers/'),
        ),
        migrations.CreateModel(
            name='LogFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dezzex_app.Customer')),
            ],
        ),
    ]
