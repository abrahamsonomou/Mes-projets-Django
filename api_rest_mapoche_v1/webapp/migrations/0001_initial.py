# Generated by Django 4.2.2 on 2023-06-28 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategorieDepense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Description')),
                ('is_active', models.BooleanField(default=True, verbose_name='status')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Create date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update date')),
            ],
        ),
        migrations.CreateModel(
            name='CategorieRevenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Description')),
                ('is_active', models.BooleanField(default=True, verbose_name='status')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Create date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update date')),
            ],
        ),
        migrations.CreateModel(
            name='Compte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=250, null=True)),
                ('numero', models.CharField(blank=True, max_length=250, null=True)),
                ('solde', models.DecimalField(decimal_places=2, max_digits=50)),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Description')),
                ('is_active', models.BooleanField(default=True, verbose_name='status')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Create date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update date')),
            ],
        ),
        migrations.CreateModel(
            name='Devise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
                ('nom', models.CharField(blank=True, max_length=100, null=True)),
                ('symbole', models.CharField(blank=True, max_length=10, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='status')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Create date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update date')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_transaction', models.CharField(choices=[('R', 'Revenu'), ('D', 'Dépense')], max_length=1)),
                ('nom', models.CharField(blank=True, max_length=250, null=True)),
                ('date', models.DateField()),
                ('montant', models.DecimalField(decimal_places=2, max_digits=20)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('C', 'Completed'), ('F', 'Failed')], default='P', max_length=1)),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Description')),
                ('is_active', models.BooleanField(default=True, verbose_name='status')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Create date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('compte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.compte')),
            ],
        ),
        migrations.CreateModel(
            name='Revenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=250, null=True)),
                ('date', models.DateField()),
                ('montant', models.DecimalField(decimal_places=2, max_digits=20)),
                ('periodicite', models.CharField(choices=[('P', 'Ponctuel'), ('Q', 'Quotidien'), ('H', 'Hebdomadaire'), ('M', 'Mensuel'), ('T', 'Trimestriel'), ('S', 'Semestriel'), ('A', 'Annuel')], max_length=1)),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Description')),
                ('is_active', models.BooleanField(default=True, verbose_name='status')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Create date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.categorierevenu')),
                ('compte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.compte')),
            ],
        ),
        migrations.CreateModel(
            name='Parametre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('valeur', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True, verbose_name='status')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Create date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('devise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.devise')),
            ],
        ),
        migrations.CreateModel(
            name='Depense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=250, null=True)),
                ('date', models.DateField()),
                ('montant', models.DecimalField(decimal_places=2, max_digits=20)),
                ('periodicite', models.CharField(choices=[('P', 'Ponctuel'), ('Q', 'Quotidien'), ('H', 'Hebdomadaire'), ('M', 'Mensuel'), ('T', 'Trimestriel'), ('S', 'Semestriel'), ('A', 'Annuel')], max_length=1)),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Description')),
                ('is_active', models.BooleanField(default=True, verbose_name='status')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Create date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.categoriedepense')),
                ('compte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.compte')),
            ],
        ),
    ]