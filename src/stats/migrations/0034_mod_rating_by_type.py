# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-02-27 15:43
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0033_award_order_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='flight_time_heavy',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='flight_time_light',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='flight_time_medium',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='rating_heavy',
            field=models.BigIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='rating_light',
            field=models.BigIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='rating_medium',
            field=models.BigIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='relive_heavy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='relive_light',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='relive_medium',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='score_heavy',
            field=models.BigIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='score_light',
            field=models.BigIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='score_medium',
            field=models.BigIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='score_streak_current_heavy',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='score_streak_current_light',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='score_streak_current_medium',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='score_streak_max_heavy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='score_streak_max_light',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='score_streak_max_medium',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='playermission',
            name='score_heavy',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='playermission',
            name='score_light',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='playermission',
            name='score_medium',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='squad',
            name='flight_time_heavy',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='squad',
            name='flight_time_light',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='squad',
            name='flight_time_medium',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='squad',
            name='rating_heavy',
            field=models.BigIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='squad',
            name='rating_light',
            field=models.BigIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='squad',
            name='rating_medium',
            field=models.BigIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='squad',
            name='relive_heavy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='squad',
            name='relive_light',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='squad',
            name='relive_medium',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='squad',
            name='score_heavy',
            field=models.BigIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='squad',
            name='score_light',
            field=models.BigIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='squad',
            name='score_medium',
            field=models.BigIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='vlife',
            name='score_heavy',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='vlife',
            name='score_light',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='vlife',
            name='score_medium',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='award',
            name='order',
            field=models.CharField(blank=True, db_index=True, default='', max_length=8, verbose_name='order field'),
        ),
        migrations.AlterField(
            model_name='object',
            name='cls',
            field=models.CharField(blank=True, choices=[('aaa_heavy', 'aaa_heavy'), ('aaa_light', 'aaa_light'), ('aaa_mg', 'aaa_mg'), ('aerostat', 'aerostat'), ('aircraft_gunner', 'aircraft_gunner'), ('aircraft_heavy', 'aircraft_heavy'), ('aircraft_light', 'aircraft_light'), ('aircraft_medium', 'aircraft_medium'), ('aircraft_pilot', 'aircraft_pilot'), ('aircraft_static', 'aircraft_static'), ('aircraft_transport', 'aircraft_transport'), ('aircraft_turret', 'aircraft_turret'), ('armoured_vehicle', 'armoured_vehicle'), ('artillery_field', 'artillery_field'), ('artillery_howitzer', 'artillery_howitzer'), ('artillery_rocket', 'artillery_rocket'), ('block', 'block'), ('bomb', 'bomb'), ('building_big', 'building_big'), ('building_medium', 'building_medium'), ('building_small', 'building_small'), ('bullet', 'bullet'), ('car', 'car'), ('driver', 'driver'), ('explosion', 'explosion'), ('locomotive', 'locomotive'), ('machine_gunner', 'machine_gunner'), ('parachute', 'parachute'), ('rocket', 'rocket'), ('searchlight', 'searchlight'), ('ship', 'ship'), ('ship_heavy', 'ship_heavy'), ('ship_light', 'ship_light'), ('ship_medium', 'ship_medium'), ('shell', 'shell'), ('tank_heavy', 'tank_heavy'), ('tank_light', 'tank_light'), ('tank_medium', 'tank_medium'), ('tank_driver', 'tank_driver'), ('tank_turret', 'tank_turret'), ('trash', 'trash'), ('truck', 'truck'), ('vehicle_crew', 'vehicle_crew'), ('vehicle_static', 'vehicle_static'), ('vehicle_turret', 'vehicle_turret'), ('wagon', 'wagon')], max_length=24),
        ),
        migrations.AlterField(
            model_name='sortie',
            name='country',
            field=models.IntegerField(choices=[(0, 'neutral'), (101, 'USSR'), (102, 'Great Britain'), (103, 'USA'), (201, 'Germany'), (202, 'Italy'), (203, 'Japan'), (301, 'France'), (302, 'Great Britain'), (303, 'USA'), (304, 'Belgium'), (305, 'Russia'), (401, 'Germany'), (402, 'Austria-Hungary')], default=0),
        ),
        migrations.AlterField(
            model_name='sortie',
            name='weapon_mods_id',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='vlife',
            name='sorties_total',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]
