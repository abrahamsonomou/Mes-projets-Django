from rest_framework import  viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from .serializers import User, UserSerializer, CompteSerializer, CategorieDepenseSerializer, RevenuSerializer \
    ,DepenseSerializer, TransactionSerializer, CategorieRevenuSerializer, DeviseSerializer, ParametreSerializer
from .models import Compte, CategorieDepense, Revenu, Depense, Transaction, CategorieRevenu, Devise, Parametre
from rest_framework.exceptions import ValidationError
from rest_framework import status
from datetime import date

config = Parametre.objects.first()

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CompteViewSet(viewsets.ModelViewSet):
    queryset = Compte.objects.all()
    serializer_class = CompteSerializer

class CategorieDepenseViewSet(viewsets.ModelViewSet):
    queryset = CategorieDepense.objects.all()
    serializer_class = CategorieDepenseSerializer

class CategorieRevenuViewSet(viewsets.ModelViewSet):
    queryset = CategorieRevenu.objects.all()
    serializer_class = CategorieRevenuSerializer

class RevenuViewSet(viewsets.ModelViewSet):
    queryset = Revenu.objects.all()
    serializer_class = RevenuSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Vérification de la date
        date = serializer.validated_data['date']
        if date > date.today():
            raise ValidationError("La date doit être inférieure ou égale à la date d'aujourd'hui.")

        # Vérification du solde
        montant = serializer.validated_data['montant']
        if montant <= 0:
            raise ValidationError("Le solde doit être strictement positif.")

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        # Vérification de la date
        date = serializer.validated_data['date']
        if date > date.today():
            raise ValidationError("La date doit être inférieure ou égale à la date d'aujourd'hui.")

        # Vérification du solde
        montant = serializer.validated_data['montant']
        if montant <= 0:
            raise ValidationError("Le solde doit être strictement positif.")

        self.perform_update(serializer)
        return Response(serializer.data)

class DepenseViewSet(viewsets.ModelViewSet):
    queryset = Depense.objects.all()
    serializer_class = DepenseSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Vérification de la date
        date = serializer.validated_data['date']
        if date > date.today():
            raise ValidationError("La date doit être inférieure ou égale à la date d'aujourd'hui.")

        # Vérification du montant
        montant = serializer.validated_data['montant']
        if montant <= 0:
            raise ValidationError("Le montant doit être strictement positif.")

        # Vérification du solde du compte
        compte = serializer.validated_data['compte']
        solde_compte = compte.solde
        if montant > solde_compte:
            # raise ValidationError("Le montant ne peut pas être supérieur au solde du compte sélectionné.")
            raise ValidationError(f"Le solde du compte {compte.nom} est insuffisant.")
        
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        # Vérification de la date
        date = serializer.validated_data['date']
        if date > date.today():
            raise ValidationError("La date doit être inférieure ou égale à la date d'aujourd'hui.")

        # Vérification du montant
        montant = serializer.validated_data['montant']
        if montant <= 0:
            raise ValidationError("Le montant doit être strictement positif.")

        # Vérification du solde du compte
        compte = serializer.validated_data['compte']
        solde_compte = compte.solde
        if montant > solde_compte:
            # raise ValidationError("Le montant ne peut pas être supérieur au solde du compte sélectionné.")
            raise ValidationError(f"Le solde du compte {compte.nom} est insuffisant.")

        self.perform_update(serializer)
        return Response(serializer.data)

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class BilanView(APIView):
    def get(self, request):
        # Récupération des paramètres d'année, de mois et de date
        annee = request.GET.get('annee')
        mois = request.GET.get('mois')
        date = request.GET.get('date')

        # Filtrage des revenus et des dépenses en fonction des paramètres
        revenus = Revenu.objects.all()
        depenses = Depense.objects.all()

        if annee:
            revenus = revenus.filter(date__year=annee)
            depenses = depenses.filter(date__year=annee)
        if mois:
            revenus = revenus.filter(date__month=mois)
            depenses = depenses.filter(date__month=mois)
        if date:
            revenus = revenus.filter(date=date)
            depenses = depenses.filter(date=date)

        # Calcul du total des revenus
        total_revenus = revenus.aggregate(total=Sum('montant'))['total']
        if total_revenus is None:
            total_revenus = 0

        # Calcul du total des dépenses
        total_depenses = depenses.aggregate(total=Sum('montant'))['total']
        if total_depenses is None:
            total_depenses = 0

        # Calcul du solde
        solde = total_revenus - total_depenses
        
        # Création du dictionnaire de résultats
        if config != "" :
            parametre = config.devise.symbole
        else:
            parametre = ""

        bilan = {
            'total_revenus': total_revenus,
            'total_depenses': total_depenses,
            'solde': solde,
            'devise': parametre,
        }

        return Response(bilan)

class DeviseViewSet(viewsets.ModelViewSet):
    queryset = Devise.objects.all()
    serializer_class = DeviseSerializer

class ParametreViewSet(viewsets.ModelViewSet):
    queryset = Parametre.objects.all()
    serializer_class = ParametreSerializer

