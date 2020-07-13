# Generated by Django 3.0.7 on 2020-06-15 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(default='India', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prop_id', models.BigIntegerField(unique=True)),
                ('prop_name', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('neighborhood', models.CharField(blank=True, max_length=255, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('bedrooms', models.SmallIntegerField(blank=True, null=True)),
                ('beds', models.SmallIntegerField(blank=True, null=True)),
                ('bathrooms', models.FloatField(blank=True, null=True)),
                ('host_languages', models.CharField(blank=True, max_length=255, null=True)),
                ('person_capacity', models.SmallIntegerField(blank=True, null=True)),
                ('public_address', models.TextField(blank=True, null=True)),
                ('amenities', models.TextField(blank=True, max_length=1024, null=True)),
                ('room_type_name', models.CharField(blank=True, max_length=255, null=True)),
                ('guest_label', models.CharField(blank=True, max_length=255, null=True)),
                ('review_count', models.IntegerField(blank=True, default=0, null=True)),
                ('star_rating', models.FloatField(blank=True, default=0, null=True)),
                ('average_rating', models.FloatField(blank=True, default=0, null=True)),
                ('location_rating', models.FloatField(blank=True, default=0, null=True)),
                ('communication_rating', models.FloatField(blank=True, default=0, null=True)),
                ('value_rating', models.FloatField(blank=True, default=0, null=True)),
                ('check_in_rating', models.FloatField(blank=True, default=0, null=True)),
                ('accuracy_rating', models.FloatField(blank=True, default=0, null=True)),
                ('cleanliness_rating', models.FloatField(blank=True, default=0, null=True)),
                ('rate_type', models.CharField(blank=True, max_length=20, null=True)),
                ('rate_amount', models.FloatField(blank=True, null=True)),
                ('rate_currency', models.CharField(blank=True, max_length=255, null=True)),
                ('price_initial', models.FloatField(blank=True, null=True)),
                ('price_initial_currency', models.CharField(blank=True, max_length=255, null=True)),
                ('cleaning_fee', models.FloatField(blank=True, max_length=10, null=True)),
                ('cleaning_fee_currency', models.CharField(blank=True, max_length=255, null=True)),
                ('min_nights', models.SmallIntegerField(blank=True, default=1, null=True)),
                ('cancel_policy', models.TextField(blank=True, null=True)),
                ('post_code', models.CharField(blank=True, max_length=255, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New Delhi', max_length=50)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Country')),
            ],
        ),
    ]
