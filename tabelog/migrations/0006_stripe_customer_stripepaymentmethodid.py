# Generated by Django 5.1 on 2024-10-08 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabelog', '0005_rename_regist_date_stripe_customer_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stripe_customer',
            name='stripePaymentMethodId',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
