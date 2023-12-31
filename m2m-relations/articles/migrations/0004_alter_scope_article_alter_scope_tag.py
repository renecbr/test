# Generated by Django 4.2.5 on 2023-10-02 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_remove_scope_tags_scope_article_scope_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='article',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='scope', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='scope', to='articles.tag'),
        ),
    ]
