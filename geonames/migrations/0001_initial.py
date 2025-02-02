# Generated by Django 2.2.3 on 2019-08-12 16:17

# import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin1Code',
            fields=[
                ('status', models.IntegerField(choices=[(0, 'Disabled'), (100, 'Enabled'), (500, 'Archived')], default=100)),
                ('geonameid', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['country', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Admin2Code',
            fields=[
                ('status', models.IntegerField(choices=[(0, 'Disabled'), (100, 'Enabled'), (500, 'Archived')], default=100)),
                ('geonameid', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=200)),
                ('admin1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin2_set', to='geonames.Admin1Code')),
            ],
            options={
                'ordering': ['country', 'admin1', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('status', models.IntegerField(choices=[(0, 'Disabled'), (100, 'Enabled'), (500, 'Archived')], default=100)),
                ('code', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Countries',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('status', models.IntegerField(choices=[(0, 'Disabled'), (100, 'Enabled'), (500, 'Archived')], default=100)),
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Currencies',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='GeonamesUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('status', models.IntegerField(choices=[(0, 'Disabled'), (100, 'Enabled'), (500, 'Archived')], default=100)),
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('iso_639_1', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Timezone',
            fields=[
                ('status', models.IntegerField(choices=[(0, 'Disabled'), (100, 'Enabled'), (500, 'Archived')], default=100)),
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('gmt_offset', models.DecimalField(decimal_places=2, max_digits=4)),
                ('dst_offset', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            options={
                'ordering': ['gmt_offset', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('status', models.IntegerField(choices=[(0, 'Disabled'), (100, 'Enabled'), (500, 'Archived')], default=100)),
                ('geonameid', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('long_name', models.CharField(max_length=200)),
                ('population', models.PositiveIntegerField()),
                ('lat', models.DecimalField(max_digits=9, decimal_places=6, null=True)),
                ('lon', models.DecimalField(max_digits=9, decimal_places=6, null=True)),
                # ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('modification_date', models.DateField()),
                ('admin1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locality_set', to='geonames.Admin1Code')),
                ('admin2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locality_set', to='geonames.Admin2Code')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locality_set', to='geonames.Country')),
                ('timezone', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locality_set', to='geonames.Timezone')),
            ],
            options={
                'verbose_name_plural': 'Localities',
                'ordering': ['country', 'admin1', 'admin2', 'long_name'],
            },
        ),
        migrations.AddField(
            model_name='country',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_set', to='geonames.Currency'),
        ),
        migrations.AddField(
            model_name='country',
            name='languages',
            field=models.ManyToManyField(related_name='country_set', to='geonames.Language'),
        ),
        migrations.AddField(
            model_name='admin2code',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin2_set', to='geonames.Country'),
        ),
        migrations.AddField(
            model_name='admin1code',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin1_set', to='geonames.Country'),
        ),
        migrations.CreateModel(
            name='AlternateName',
            fields=[
                ('status', models.IntegerField(choices=[(0, 'Disabled'), (100, 'Enabled'), (500, 'Archived')], default=100)),
                ('alternatenameid', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('locality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alternatename_set', to='geonames.Locality')),
            ],
            options={
                'ordering': ['locality__pk', 'name'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='admin2code',
            unique_together={('country', 'admin1', 'name')},
        ),
        migrations.AlterUniqueTogether(
            name='admin1code',
            unique_together={('country', 'name')},
        ),
    ]
