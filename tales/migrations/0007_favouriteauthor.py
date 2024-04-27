# Generated by Django 4.0.6 on 2024-04-22 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tales', '0006_likedscribes'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavouriteAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorId', models.CharField(db_column='authorId', max_length=255)),
                ('readerId', models.ForeignKey(db_column='readerId', on_delete=django.db.models.deletion.CASCADE, to='tales.userprofile')),
                ('scribeId', models.ForeignKey(db_column='scribeId', null=True, on_delete=django.db.models.deletion.SET_NULL, to='tales.scribes')),
            ],
            options={
                'unique_together': {('readerId', 'authorId')},
            },
        ),
    ]
