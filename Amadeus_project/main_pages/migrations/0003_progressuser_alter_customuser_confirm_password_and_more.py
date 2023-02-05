# Generated by Django 4.1.5 on 2023-02-03 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_pages', '0002_customuser_confirm_password_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgressUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='confirm_password',
            field=models.CharField(blank=True, max_length=100, verbose_name='Подтвеждение пароля'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.CharField(max_length=100, unique=True, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=100, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=50, unique=True, verbose_name='Логин'),
        ),
    ]
