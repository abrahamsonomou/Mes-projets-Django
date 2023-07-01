from django.core.management.base import BaseCommand
from webapp.models import CategorieRevenu

class Command(BaseCommand):
    help = 'Création des catégories de revenus'

    def handle(self, *args, **options):
        categories = [
            {'nom': 'Salaire', 'description': 'Revenus provenant d\'un salaire'},
            {'nom': 'Freelance', 'description': 'Revenus provenant de missions en freelance'},
            {'nom': 'Investissements', 'description': 'Revenus provenant d\'investissements'},
            {'nom': 'Vente en ligne', 'description': 'Revenus provenant de ventes en ligne'},
            {'nom': 'Location', 'description': 'Revenus provenant de la location d\'un bien'},
            {'nom': 'Dividendes', 'description': 'Revenus provenant de dividendes d\'actions'},
            {'nom': 'Pension', 'description': 'Revenus provenant d\'une pension'},
            {'nom': 'Bourse', 'description': 'Revenus provenant du trading en bourse'},
            {'nom': 'Cours particuliers', 'description': 'Revenus provenant de cours particuliers'},
            {'nom': 'Rémunération artistique', 'description': 'Revenus provenant d\'activités artistiques'},
            {'nom': 'Revenus locatifs', 'description': 'Revenus provenant de la location de biens immobiliers'},
            {'nom': 'Prime', 'description': 'Revenus sous forme de prime'},
            {'nom': 'Remboursement', 'description': 'Revenus provenant de remboursements'},
            {'nom': 'Subvention', 'description': 'Revenus sous forme de subvention'},
            {'nom': 'Héritage', 'description': 'Revenus provenant d\'un héritage'},
            {'nom': 'Gains de jeu', 'description': 'Revenus provenant de gains de jeu'},
            {'nom': 'Partenariats', 'description': 'Revenus provenant de partenariats'},
            {'nom': 'Consulting', 'description': 'Revenus provenant de services de consulting'},
            {'nom': 'Publicité', 'description': 'Revenus provenant de la publicité'},
            {'nom': 'Autres', 'description': 'Autres sources de revenus'},
        ]

        for categorie_data in categories:
            categorie = CategorieRevenu.objects.create(
                nom=categorie_data['nom'],
                description=categorie_data['description'],
            )
            self.stdout.write(self.style.SUCCESS(f'Catégorie "{categorie.nom}" créée avec succès.'))

        self.stdout.write(self.style.SUCCESS('Création des catégories de revenus terminée avec succès.'))
