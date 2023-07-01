from django.core.management.base import BaseCommand
from webapp.models import Compte

class Command(BaseCommand):
    help = 'Création des comptes'

    def handle(self, *args, **options):
        comptes = [
            {'nom': 'Compte courant', 'numero': '001', 'solde': 5000, 'description': 'Compte pour les transactions courantes'},
            {'nom': 'Compte d\'épargne', 'numero': '002', 'solde': 10000, 'description': 'Compte pour épargner de l\'argent'},
            {'nom': 'Compte chèques', 'numero': '003', 'solde': 2000, 'description': 'Compte associé à des chèques'},
            {'nom': 'Compte carte de crédit', 'numero': '004', 'solde': 500, 'description': 'Compte pour les dépenses à crédit'},
            {'nom': 'Compte à terme', 'numero': '005', 'solde': 15000, 'description': 'Compte à taux fixe pour une durée spécifiée'},
            {'nom': 'Compte de dépôt à vue', 'numero': '006', 'solde': 3000, 'description': 'Compte avec accès facile aux fonds déposés'},
            {'nom': 'Compte IRA', 'numero': '007', 'solde': 50000, 'description': 'Compte pour l\'épargne-retraite'},
            {'nom': 'Compte de dépôt à terme', 'numero': '008', 'solde': 10000, 'description': 'Compte avec taux d\'intérêt fixe'},
            {'nom': 'Compte de dépôt à vue à intérêt élevé', 'numero': '009', 'solde': 8000, 'description': 'Compte courant avec un taux d\'intérêt plus élevé'},
            {'nom': 'Compte du marché monétaire', 'numero': '010', 'solde': 25000, 'description': 'Compte avec des rendements similaires au marché monétaire'},
            # Ajoutez d'autres comptes avec leurs numéros correspondants
        ]

        for compte_data in comptes:
            compte = Compte.objects.create(
                nom=compte_data['nom'],
                numero=compte_data['numero'],
                solde=compte_data['solde'],
                description=compte_data['description'],
            )
            self.stdout.write(self.style.SUCCESS(f'Compte "{compte.nom}" (Numéro de compte : {compte.numero}) créé avec succès.'))

        self.stdout.write(self.style.SUCCESS('Création des comptes terminée avec succès.'))
