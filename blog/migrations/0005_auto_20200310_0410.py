# Generated by Django 3.0.3 on 2020-03-10 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200310_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('WO', 'Work'), ('BU', 'Business'), ('FD', 'Food'), ('MV', 'Movies'), ('BK', 'Books'), ('MO', 'Mom'), ('TR', 'Travel'), ('LS', 'Lifestyle'), ('DI', 'Diy'), ('PA', 'Parenting'), ('GR', 'General'), ('SC', 'Social')], default='GR', max_length=255),
        ),
    ]