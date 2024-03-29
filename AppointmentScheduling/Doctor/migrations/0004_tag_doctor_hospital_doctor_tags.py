# Generated by Django 4.2.5 on 2023-09-21 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0001_initial'),
        ('Doctor', '0003_rename_operatingdays_operatingday_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='hospital',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Hospital.hospital'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='tags',
            field=models.ManyToManyField(blank=True, to='Doctor.tag'),
        ),
    ]
