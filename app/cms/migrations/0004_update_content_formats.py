"""
Migration to update content format choices from HTML to Markdown/Plain Text.
Removes HTML as an option and sets Markdown as the default.
"""

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_add_content_format'),
    ]

    operations = [
        # Update Document model content_format field
        migrations.AlterField(
            model_name='document',
            name='content_format',
            field=models.CharField(
                choices=[('markdown', 'Markdown'), ('plaintext', 'Plain Text')],
                default='markdown',
                max_length=10,
                verbose_name='Content Format'
            ),
        ),
        
        # Update DocumentVersion model content_format field
        migrations.AlterField(
            model_name='documentversion',
            name='content_format',
            field=models.CharField(
                choices=[('markdown', 'Markdown'), ('plaintext', 'Plain Text')],
                default='markdown',
                max_length=10,
                verbose_name='Content Format'
            ),
        ),
        
        # Data migration to convert existing HTML content to Markdown
        # Since this is a dev database with no real data, we're just
        # updating the content_format field value without converting content
        migrations.RunSQL(
            """
            UPDATE cms_document 
            SET content_format = 'markdown' 
            WHERE content_format = 'html';
            
            UPDATE cms_documentversion 
            SET content_format = 'markdown' 
            WHERE content_format = 'html';
            """,
            reverse_sql="""
            -- No reverse migration needed for dev database
            """
        ),
    ]
