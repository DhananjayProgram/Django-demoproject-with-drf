# Generated by Django 5.0.6 on 2024-06-06 11:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("task_name", models.CharField(max_length=20)),
                ("task_description", models.CharField(max_length=50)),
                ("assignTaskDate", models.DateTimeField(auto_now=True)),
                ("deadline", models.DateTimeField()),
                (
                    "important",
                    models.CharField(
                        choices=[("normal", "Normal"), ("hot", "Hot")],
                        default="normal",
                        max_length=25,
                    ),
                ),
                (
                    "task_status",
                    models.CharField(
                        choices=[
                            ("complete", "Complete Task"),
                            ("ongoing", "Ongoing Task"),
                            ("pending", "Not Started"),
                        ],
                        default="pending",
                        max_length=25,
                    ),
                ),
                (
                    "User",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
