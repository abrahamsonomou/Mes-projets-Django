from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

# Create your models here.
class MyCustomManager(models.Manager):
    def all(self, is_active=True):
        queryset = super().get_queryset()
        if is_active:
            queryset = queryset.filter(is_active=True)
        return queryset

class Compte(models.Model):
    nom = models.CharField(max_length=250, blank=True, null=True)
    numero = models.CharField(max_length=250, blank=True, null=True)
    solde = models.DecimalField(max_digits=50, decimal_places=2)
    description = models.CharField(max_length=200, verbose_name="Description", blank=True, null=True)

    is_active=models.BooleanField(default=True,verbose_name="status")
    created_at=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated_at=models.DateTimeField(auto_now=True,verbose_name='Update date')

    objects = MyCustomManager()

    def __str__(self) -> str:
        return f"{self.nom} - {self.numero}"

class CategorieDepense(models.Model):
    nom = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=200, verbose_name="Description", blank=True, null=True)

    is_active=models.BooleanField(default=True,verbose_name="status")
    created_at=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated_at=models.DateTimeField(auto_now=True,verbose_name='Update date')

    objects = MyCustomManager()

    def __str__(self) -> str:
        return self.nom

class CategorieRevenu(models.Model):
    nom = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=200, verbose_name="Description", blank=True, null=True)

    is_active=models.BooleanField(default=True,verbose_name="status")
    created_at=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated_at=models.DateTimeField(auto_now=True,verbose_name='Update date')

    objects = MyCustomManager()

    def __str__(self) -> str:
        return self.nom
            
class Revenu(models.Model):
    PERIODICITE_CHOICES = (
        ('P', 'Ponctuel'),
        ('Q', 'Quotidien'),
        ('H', 'Hebdomadaire'),
        ('M', 'Mensuel'),
        ('T', 'Trimestriel'),
        ('S', 'Semestriel'),
        ('A', 'Annuel'),
    )

    compte = models.ForeignKey(Compte, on_delete=models.CASCADE)
    nom = models.CharField(max_length=250, blank=True, null=True)
    date = models.DateField()
    montant = models.DecimalField(max_digits=20, decimal_places=2)
    periodicite = models.CharField(max_length=1, choices=PERIODICITE_CHOICES)
    description = models.CharField(max_length=200, verbose_name="Description", blank=True, null=True)
    categorie = models.ForeignKey(CategorieRevenu, on_delete=models.CASCADE)

    is_active=models.BooleanField(default=True,verbose_name="status")
    created_at=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated_at=models.DateTimeField(auto_now=True,verbose_name='Update date')

    def save(self, *args, **kwargs):
        self.compte.solde += self.montant
        self.compte.save()
        super().save(*args, **kwargs)

    objects = MyCustomManager()

    def __str__(self) -> str:
        return self.nom
    
class Depense(models.Model):
    PERIODICITE_CHOICES = (
        ('P', 'Ponctuel'),
        ('Q', 'Quotidien'),
        ('H', 'Hebdomadaire'),
        ('M', 'Mensuel'),
        ('T', 'Trimestriel'),
        ('S', 'Semestriel'),
        ('A', 'Annuel'),
    )

    compte = models.ForeignKey(Compte, on_delete=models.CASCADE)
    nom = models.CharField(max_length=250, blank=True, null=True)
    date = models.DateField()
    montant = models.DecimalField(max_digits=20, decimal_places=2)
    periodicite = models.CharField(max_length=1, choices=PERIODICITE_CHOICES)
    categorie = models.ForeignKey(CategorieDepense, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, verbose_name="Description", blank=True, null=True)

    is_active=models.BooleanField(default=True,verbose_name="status")
    created_at=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated_at=models.DateTimeField(auto_now=True,verbose_name='Update date')

    objects = MyCustomManager()

    def save(self, *args, **kwargs):
        self.compte.solde -= self.montant
        self.compte.save()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.nom
    
class Transaction(models.Model):
    TYPE_CHOICES = (
        ('R', 'Revenu'),
        ('D', 'Dépense'),
    )

    STATUS_CHOICES = (
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('F', 'Failed'),
    )

    compte = models.ForeignKey(Compte, on_delete=models.CASCADE)
    type_transaction = models.CharField(max_length=1, choices=TYPE_CHOICES)
    nom = models.CharField(max_length=250, blank=True, null=True)
    date = models.DateField()
    montant = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    description = models.CharField(max_length=200, verbose_name="Description", blank=True, null=True)

    is_active=models.BooleanField(default=True,verbose_name="status")
    created_at=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated_at=models.DateTimeField(auto_now=True,verbose_name='Update date')

    objects = MyCustomManager()

    def __str__(self) -> str:
        return self.nom

class Devise(models.Model):
    code = models.CharField(max_length=10, blank=True, null=True)
    nom = models.CharField(max_length=100, blank=True, null=True)
    symbole = models.CharField(max_length=10, blank=True, null=True)

    is_active=models.BooleanField(default=True,verbose_name="status")
    created_at=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated_at=models.DateTimeField(auto_now=True,verbose_name='Update date')

    objects = MyCustomManager()

    def __str__(self):
        return self.nom

class Parametre(models.Model):
    nom = models.CharField(max_length=100)
    valeur = models.CharField(max_length=200)
    devise = models.ForeignKey(Devise, on_delete=models.CASCADE)

    is_active=models.BooleanField(default=True,verbose_name="status")
    created_at=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated_at=models.DateTimeField(auto_now=True,verbose_name='Update date')

    objects = MyCustomManager()

    def __str__(self):
        return self.nom
    
