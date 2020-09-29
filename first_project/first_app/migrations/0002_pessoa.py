# Generated by Django 3.0.3 on 2020-09-29 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('url', models.URLField(unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('referencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.Topico')),
                ('webpage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.Webpage')),
            ],
        ),
    ]
