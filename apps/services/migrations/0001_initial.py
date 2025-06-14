# Generated by Django 5.2 on 2025-06-07 13:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('equipments', '0001_initial'),
        ('technicians', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitacaoServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_solicitacao', models.DateField(auto_now_add=True)),
                ('descricao', models.TextField()),
                ('status', models.CharField(choices=[('PENDENTE', 'Pendente'), ('ATRIBUIDA', 'Atribuída'), ('EM_ANDAMENTO', 'Em andamento'), ('CONCLUIDA', 'Concluída'), ('CANCELADA', 'Cancelada')], default='PENDENTE', max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.cliente')),
                ('equipamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipments.equipamento')),
                ('tecnico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='technicians.tecnico')),
            ],
        ),
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('periodo_horario', models.CharField(max_length=50)),
                ('solicitacao', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='services.solicitacaoservico')),
            ],
        ),
    ]
