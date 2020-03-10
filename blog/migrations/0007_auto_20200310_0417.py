# Generated by Django 3.0.3 on 2020-03-10 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200310_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('General', 'General'), ('Work', 'Work'), ('Business', 'Business'), ('Food', 'Food'), ('Movies', 'Movies'), ('Books', 'Books'), ('Mom', 'Mom'), ('Travel', 'Travel'), ('Lifestyle', 'Lifestyle'), ('DIY', 'Diy'), ('Parenting', 'Parenting'), ('Social', 'Social'), ('Study', 'Study'), ('Daily', 'Daily')], default='General', max_length=255),
        ),
    ]
