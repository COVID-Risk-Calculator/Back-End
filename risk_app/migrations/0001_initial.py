# Generated by Django 4.1.1 on 2022-09-14 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tested', models.TextField(choices=[('None', 'none'), ('PCR', 'pcr'), ('Rapid At-Home', 'rapid-at-home'), ('Rapid Medically-Administered', 'rapid-medical')], default='None')),
                ('test_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(max_length=255, null=True)),
                ('case_data', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('vaccination_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('risk_mutliplier', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('first_name', models.CharField(max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='geusts', to='risk_app.test')),
            ],
        ),
    ]
