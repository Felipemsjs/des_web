# Generated by Django 3.1.4 on 2023-12-05 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0005_dados_departamento_projeto'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='departamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard_app.departamento'),
        ),
    ]