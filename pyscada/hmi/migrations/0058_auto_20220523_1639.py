# Generated by Django 3.2 on 2022-05-23 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hmi', '0057_auto_20211214_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('base_filename', models.CharField(default='base', help_text="Enter the filename without '.html'", max_length=400)),
                ('view_filename', models.CharField(default='view', help_text="Enter the filename without '.html'", max_length=400)),
            ],
        ),
        migrations.AddField(
            model_name='view',
            name='theme',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hmi.theme'),
        ),
    ]
