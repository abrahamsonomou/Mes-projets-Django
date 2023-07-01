from django.core.management.base import BaseCommand
from webapp.models import CategorieDepense

class Command(BaseCommand):
    help = 'Création des catégories de dépenses'

    def handle(self, *args, **options):
        categories = [
            {'nom': 'Alimentation', 'description': 'Dépenses liées à l\'achat de nourriture'},
            {'nom': 'Transport', 'description': 'Dépenses liées aux frais de transport'},
            {'nom': 'Logement', 'description': 'Dépenses liées au loyer ou à l\'hypothèque'},
            {'nom': 'Santé', 'description': 'Dépenses liées aux frais médicaux'},
            {'nom': 'Éducation', 'description': 'Dépenses liées aux frais scolaires ou universitaires'},
            {'nom': 'Divertissement', 'description': 'Dépenses liées aux loisirs et aux divertissements'},
            {'nom': 'Voyages', 'description': 'Dépenses liées aux frais de voyage'},
            {'nom': 'Vêtements', 'description': 'Dépenses liées à l\'achat de vêtements'},
            {'nom': 'Épicerie', 'description': 'Dépenses liées aux courses alimentaires'},
            {'nom': 'Assurance', 'description': 'Dépenses liées aux primes d\'assurance'},
            {'nom': 'Factures', 'description': 'Dépenses liées aux factures de services publics'},
            {'nom': 'Loisirs', 'description': 'Dépenses liées aux activités de loisirs'},
            {'nom': 'Télécommunications', 'description': 'Dépenses liées aux frais de télécommunications'},
            {'nom': 'Frais bancaires', 'description': 'Dépenses liées aux frais bancaires'},
            {'nom': 'Cadeaux', 'description': 'Dépenses liées aux cadeaux et aux présents'},
            {'nom': 'Restaurant', 'description': 'Dépenses liées aux repas pris au restaurant'},
            {'nom': 'Services professionnels', 'description': 'Dépenses liées aux services professionnels'},
            {'nom': 'Automobile', 'description': 'Dépenses liées à l\'entretien et à l\'essence de la voiture'},
            {'nom': 'Énergie', 'description': 'Dépenses liées à l\'électricité et au chauffage'},
            {'nom': 'Frais financiers', 'description': 'Dépenses liées aux frais financiers'},
            # Ajoutez d'autres catégories selon vos besoins
        ]

        for categorie_data in categories:
            categorie = CategorieDepense.objects.create(
                nom=categorie_data['nom'],
                description=categorie_data['description'],
            )
            self.stdout.write(self.style.SUCCESS(f'Catégorie "{categorie.nom}" créée avec succès.'))

        self.stdout.write(self.style.SUCCESS('Création des catégories de dépenses terminée avec succès.'))
