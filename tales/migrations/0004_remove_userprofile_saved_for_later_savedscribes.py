# Generated by Django 4.0.6 on 2024-04-22 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tales', '0003_userprofile_saved_for_later'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='saved_for_later',
        ),
        migrations.CreateModel(
            name='SavedScribes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scribeId', models.ForeignKey(db_column='scribeId', null=True, on_delete=django.db.models.deletion.SET_NULL, to='tales.scribes')),
                ('userId', models.ForeignKey(db_column='userId', null=True, on_delete=django.db.models.deletion.SET_NULL, to='tales.userprofile')),
            ],
        ),
    ]
