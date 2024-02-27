from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='owner_id',
            new_name='owner',
        ),
        migrations.RemoveField(
            model_name='product',
            name='owner_id',  # Указываем имя старого поля, которое нужно удалить
        ),
    ]
