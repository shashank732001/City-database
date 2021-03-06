# Generated by Django 4.0.4 on 2022-05-19 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oh', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City_add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oh.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oh.country')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oh.district')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oh.state')),
            ],
        ),
    ]
