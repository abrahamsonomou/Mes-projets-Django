# Dans le fichier load_devises.py

from django.core.management.base import BaseCommand
from webapp.models import Devise


class Command(BaseCommand):
    help = 'Charge les devises dans la table Devise'

    def handle(self, *args, **options):
        devises = [
            {'code': 'DZD', 'nom': 'Dinar algérien', 'symbole': 'د.ج'},
            {'code': 'AOA', 'nom': 'Kwanza angolais', 'symbole': 'Kz'},
            {'code': 'XOF', 'nom': 'Franc CFA (BCEAO)', 'symbole': 'CFA'},
            {'code': 'BWP', 'nom': 'Pula botswanaise', 'symbole': 'P'},
            {'code': 'BIF', 'nom': 'Franc burundais', 'symbole': 'FBu'},
            {'code': 'CVE', 'nom': 'Escudo cap-verdien', 'symbole': 'CVE'},
            {'code': 'XAF', 'nom': 'Franc CFA (BEAC)', 'symbole': 'FCFA'},
            {'code': 'KMF', 'nom': 'Franc comorien', 'symbole': 'CF'},
            {'code': 'CDF', 'nom': 'Franc congolais', 'symbole': 'FC'},
            {'code': 'DJF', 'nom': 'Franc djiboutien', 'symbole': 'Fdj'},
            {'code': 'EGP', 'nom': 'Livre égyptienne', 'symbole': '£'},
            {'code': 'ERN', 'nom': 'Nakfa érythréen', 'symbole': 'Nfk'},
            {'code': 'ETB', 'nom': 'Birr éthiopien', 'symbole': 'Br'},
            {'code': 'GMD', 'nom': 'Dalasi gambien', 'symbole': 'D'},
            {'code': 'GHS', 'nom': 'Cedi ghanéen', 'symbole': '₵'},
            {'code': 'GNF', 'nom': 'Franc guinéen', 'symbole': 'GNF'},
            {'code': 'XOF', 'nom': 'Franc guinéen-bissau', 'symbole': 'CFA'},
            {'code': 'KES', 'nom': 'Shilling kényan', 'symbole': 'KSh'},
            {'code': 'LSL', 'nom': 'Loti', 'symbole': 'L'},
            {'code': 'LRD', 'nom': 'Dollar libérien', 'symbole': 'L$'},
            {'code': 'LYD', 'nom': 'Dinar libyen', 'symbole': 'LD'},
            {'code': 'MGA', 'nom': 'Ariary malgache', 'symbole': 'Ar'},
            {'code': 'MWK', 'nom': 'Kwacha malawien', 'symbole': 'MK'},
            {'code': 'MUR', 'nom': 'Roupie mauricienne', 'symbole': '₨'},
            {'code': 'MAD', 'nom': 'Dirham marocain', 'symbole': 'د.م.'},
            {'code': 'MZN', 'nom': 'Metical mozambicain', 'symbole': 'MT'},
            {'code': 'NAD', 'nom': 'Dollar namibien', 'symbole': 'N$'},
            {'code': 'XOF', 'nom': 'Franc CFA (BCEAO)', 'symbole': 'CFA'},
            {'code': 'NGN', 'nom': 'Naira nigérian', 'symbole': '₦'},
            {'code': 'RWF', 'nom': 'Franc rwandais', 'symbole': 'FRw'},
            {'code': 'SHP', 'nom': 'Livre de Sainte-Hélène', 'symbole': '£'},
            {'code': 'STD', 'nom': 'Dobra santoméen', 'symbole': 'Db'},
            {'code': 'XOF', 'nom': 'Franc CFA (BCEAO)', 'symbole': 'CFA'},
            {'code': 'SCR', 'nom': 'Roupie seychelloise', 'symbole': '₨'},
            {'code': 'SLL', 'nom': 'Leone sierra-léonais', 'symbole': 'Le'},
            {'code': 'SOS', 'nom': 'Shilling somalien', 'symbole': 'S'},
            {'code': 'ZAR', 'nom': 'Rand sud-africain', 'symbole': 'R'},
            {'code': 'SSP', 'nom': 'Livre sud-soudanaise', 'symbole': '£'},
            {'code': 'SZL', 'nom': 'Lilangeni swazi', 'symbole': 'L'},
            {'code': 'TZS', 'nom': 'Shilling tanzanien', 'symbole': 'TSh'},
            {'code': 'XOF', 'nom': 'Franc CFA (BCEAO)', 'symbole': 'CFA'},
            {'code': 'TND', 'nom': 'Dinar tunisien', 'symbole': 'د.ت'},
            {'code': 'UGX', 'nom': 'Shilling ougandais', 'symbole': 'USh'},
            {'code': 'ZMW', 'nom': 'Kwacha zambien', 'symbole': 'ZK'},
            {'code': 'ZWL', 'nom': 'Dollar zimbabwéen', 'symbole': 'Z$'},
            {'code': 'GQE', 'nom': 'Franc équato-guinéen', 'symbole': 'CFA'},
            {'code': 'SDG', 'nom': 'Livre soudanaise', 'symbole': 'ج.س.'},
            {'code': 'TMT', 'nom': 'Manat turkmène', 'symbole': 'T'},
            {'code': 'AED', 'nom': 'Dirham des Émirats arabes unis', 'symbole': 'د.إ'},
        ]


        for devise in devises:
            Devise.objects.create(
                code=devise['code'],
                nom=devise['nom'],
                symbole=devise['symbole']
            )

        self.stdout.write(self.style.SUCCESS('Les devises ont été ajoutées avec succès.'))
