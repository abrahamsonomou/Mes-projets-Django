from rest_framework import serializers
from .models import Compte, CategorieDepense, Revenu, Depense, Transaction, CategorieRevenu, Devise, Parametre
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_staff']

class CompteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compte
        fields = '__all__'

class CategorieDepenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorieDepense
        fields = '__all__'

class RevenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenu
        fields = '__all__'

class DepenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depense
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class CategorieRevenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorieRevenu
        fields = '__all__'

class DeviseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devise
        fields = '__all__'

class ParametreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parametre
        fields = '__all__'