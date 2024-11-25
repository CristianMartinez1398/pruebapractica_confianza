# Generated by Django 5.1.3 on 2024-11-25 21:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ask',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('description', models.TextField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=80)),
                ('id_number', models.CharField(max_length=15, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ask_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='surveys.ask')),
            ],
        ),
        migrations.CreateModel(
            name='Voting',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('answer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.answer')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.user')),
            ],
            options={
                'unique_together': {('answer_id', 'user_id')},
            },
        ),
    ]