# Generated by Django 2.2.24 on 2021-10-21 05:39

# Django imports
import django.core.serializers.json
from django.db import migrations
from django.db import models

try:
    # Django imports
    from django.db.models import JSONField  # type: ignore
except ImportError:
    from django_jsonfield_backport.models import JSONField  # type: ignore

# Django imports
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [("contenttypes", "0002_remove_content_type_name")]

    operations = [
        migrations.CreateModel(
            name="FetchHistory",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_fetch_dt",
                    models.DateTimeField(
                        auto_now=True, verbose_name="last fetch datetime"
                    ),
                ),
                ("app", models.CharField(max_length=50, verbose_name="dalec app")),
                (
                    "content_type",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="content type",
                    ),
                ),
                (
                    "channel",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="channel"
                    ),
                ),
                (
                    "channel_object",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="channel app object id",
                    ),
                ),
            ],
            options={
                "verbose_name": "Content fetch history line",
                "verbose_name_plural": "Content fetch history lines",
                "ordering": ("-last_fetch_dt",),
                "get_latest_by": "last_fetch_dt",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Content",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_update_dt",
                    models.DateTimeField(
                        db_index=True,
                        verbose_name="last update datetime (on external source)",
                    ),
                ),
                (
                    "creation_dt",
                    models.DateTimeField(
                        db_index=True,
                        verbose_name="created datetime (on external source)",
                    ),
                ),
                ("app", models.CharField(max_length=50, verbose_name="dalec app")),
                (
                    "content_type",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="content type",
                    ),
                ),
                (
                    "channel",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="channel"
                    ),
                ),
                (
                    "channel_object",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="channel app object id",
                    ),
                ),
                (
                    "dj_channel_id",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="The django's model's instance which is concerned.(eg. could be an instance of model `Project` for app=gitlab, content_type=issue, channel=project)",
                        null=True,
                        verbose_name="related object",
                    ),
                ),
                (
                    "dj_content_id",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="The django's model's instance which is concerned (eg. could be an instance of model `Issue` for dalec-gitlab)",
                        null=True,
                        verbose_name="content",
                    ),
                ),
                (
                    "content_id",
                    models.CharField(
                        help_text="ID of the content inside the external app.",
                        max_length=255,
                        verbose_name="app's content id",
                    ),
                ),
                (
                    "content_data",
                    JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                (
                    "dj_channel_content_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="contenttypes.ContentType",
                    ),
                ),
                (
                    "dj_content_content_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="contenttypes.ContentType",
                    ),
                ),
            ],
            options={
                "verbose_name": "Content",
                "verbose_name_plural": "Contents",
                "ordering": ("-last_update_dt",),
                "get_latest_by": "last_update_dt",
                "abstract": False,
                "index_together": {("app", "content_type", "channel")},
            },
        ),
    ]
