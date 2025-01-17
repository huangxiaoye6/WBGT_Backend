# Generated by Django 4.2.16 on 2024-10-17 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                (
                    "username",
                    models.CharField(max_length=11, unique=True, verbose_name="账号"),
                ),
                ("password", models.CharField(max_length=64, verbose_name="密码")),
                ("uid", models.CharField(max_length=64, verbose_name="用户唯一标识")),
            ],
            options={
                "db_table": "user",
            },
        ),
    ]
