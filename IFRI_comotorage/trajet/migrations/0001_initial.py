# Generated by Django 5.2.2 on 2025-06-18 20:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trajet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('conducteur', 'Conducteur'), ('passager', 'Passager')], max_length=20)),
                ('recurring', models.BooleanField(default=False, help_text='True si trajet quotidien')),
                ('date', models.DateField(blank=True, help_text='Date du trajet pour trajet ponctuel', null=True)),
                ('heure', models.TimeField(help_text='Heure de départ')),
                ('lieu_depart', models.CharField(max_length=150)),
                ('latitude_depart', models.FloatField()),
                ('longitude_depart', models.FloatField()),
                ('lieu_arrivee', models.CharField(editable=False, max_length=150)),
                ('latitude_arrivee', models.FloatField(editable=False)),
                ('longitude_arrivee', models.FloatField(editable=False)),
                ('nb_places', models.PositiveIntegerField(blank=True, null=True)),
                ('commentaire', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('open', 'Ouvert'), ('matched', 'Apparié'), ('cancelled', 'Annulé')], default='open', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trajets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_accepted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('demande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_demande', to='trajet.trajet')),
                ('offre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_offre', to='trajet.trajet')),
            ],
            options={
                'unique_together': {('offre', 'demande')},
            },
        ),
    ]
