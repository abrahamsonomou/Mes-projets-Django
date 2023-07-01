from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Revenu, Depense, Transaction
from django.db import transaction

@receiver(post_save, sender=Revenu)
def create_revenu_transaction(sender, instance, created, **kwargs):
    if created:
        try:
            with transaction.atomic():
                transaction = Transaction(
                    compte=instance.compte,
                    type_transaction='R',
                    nom=instance.nom,
                    date=instance.date,
                    montant=instance.montant,
                    status='C'  # Transaction created successfully
                )
                transaction.save()
        except Exception as e:
            transaction = Transaction(
                compte=instance.compte,
                type_transaction='R',
                nom=instance.nom,
                date=instance.date,
                montant=instance.montant,
                status='F'  # Transaction creation failed
            )
            transaction.save()
    else:
        transaction = Transaction(
            compte=instance.compte,
            type_transaction='R',
            nom=instance.nom,
            date=instance.date,
            montant=instance.montant,
            status='F'  # Transaction creation failed
        )
        transaction.save()

@receiver(post_save, sender=Depense)
def create_depense_transaction(sender, instance, created, **kwargs):
    if created:
        try:
            with transaction.atomic():
                transaction = Transaction(
                    compte=instance.compte,
                    type_transaction='D',
                    nom=instance.nom,
                    date=instance.date,
                    montant=instance.montant,
                    status='C'  # Transaction created successfully
                )
                transaction.save()
        except Exception as e:
            transaction = Transaction(
                compte=instance.compte,
                type_transaction='D',
                nom=instance.nom,
                date=instance.date,
                montant=instance.montant,
                status='F'  # Transaction creation failed
            )
            transaction.save()
    else:
        transaction = Transaction(
            compte=instance.compte,
            type_transaction='D',
            nom=instance.nom,
            date=instance.date,
            montant=instance.montant,
            status='F'  # Transaction creation failed
        )
        transaction.save()
