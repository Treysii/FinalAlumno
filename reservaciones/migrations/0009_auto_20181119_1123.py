# Generated by Django 2.1 on 2018-11-19 17:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservaciones', '0008_auto_20181107_0030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_publicacions', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('seccion', models.CharField(max_length=30)),
                ('fechaH', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('creditos', models.IntegerField()),
                ('fecha', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='huesped',
            name='habitaciones',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='habitacion',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='huesped',
        ),
        migrations.DeleteModel(
            name='Habitacion',
        ),
        migrations.DeleteModel(
            name='Huesped',
        ),
        migrations.DeleteModel(
            name='Reserva',
        ),
        migrations.AddField(
            model_name='grado',
            name='materias',
            field=models.ManyToManyField(through='reservaciones.Asignacion', to='reservaciones.Materia'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='grado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservaciones.Grado'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservaciones.Materia'),
        ),
    ]
