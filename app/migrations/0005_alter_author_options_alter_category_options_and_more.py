# Generated by Django 4.1.7 on 2023-04-18 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_alter_comment_post"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="author",
            options={"ordering": ["created_date"]},
        ),
        migrations.AlterModelOptions(
            name="category",
            options={"ordering": ["title"], "verbose_name_plural": "Categories"},
        ),
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["comment"]},
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["posted_date"]},
        ),
        migrations.AlterModelOptions(
            name="tag",
            options={"ordering": ["title"]},
        ),
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                default=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="authors",
                to="app.author",
            ),
        ),
    ]
