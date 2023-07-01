from django.shortcuts import render
from django.db.models import Sum
from django.db.models.functions import TruncYear, TruncMonth, TruncDay
from datetime import datetime
from .models import Transaction, Compte

def simuler_bilan(request):
    # Calcul du total des revenus
    total_revenus = Transaction.objects.filter(type_transaction='R').aggregate(Sum('montant'))['montant__sum']
    total_revenus = total_revenus if total_revenus else 0
    
    # Calcul du total des dépenses
    total_depenses = Transaction.objects.filter(type_transaction='D').aggregate(Sum('montant'))['montant__sum']
    total_depenses = total_depenses if total_depenses else 0
    
    # Calcul du solde total du compte
    solde_total = Compte.objects.aggregate(Sum('solde'))['solde__sum']
    solde_total = solde_total if solde_total else 0
    
    # Calcul du solde net (revenus - dépenses)
    solde_net = total_revenus - total_depenses
    
    context= {
        'total_revenus': total_revenus,
        'total_depenses': total_depenses,
        'solde_total': solde_total,
        'solde_net': solde_net,
    }

    return render(request, 'simuler_bilan.html', context)

def bilan(request):
    # Récupération des paramètres du formulaire
    annee = request.GET.get('annee')
    mois = request.GET.get('mois')
    date = request.GET.get('date')
    
    # Filtrage des transactions selon l'année, le mois et la date choisis
    transactions = Transaction.objects.all()
    if annee:
        transactions = transactions.filter(date__year=annee)
    if mois:
        transactions = transactions.filter(date__month=mois)
    if date:
        transactions = transactions.filter(date__date=date)
    
    # Calcul du bilan par année
    bilan_par_annee = transactions.annotate(year=TruncYear('date')).values('year').annotate(total=Sum('montant')).order_by('year')
    
    # Calcul du bilan par mois
    bilan_par_mois = transactions.annotate(month=TruncMonth('date')).values('month').annotate(total=Sum('montant')).order_by('month')
    
    # Calcul du bilan par jour
    bilan_par_jour = transactions.annotate(day=TruncDay('date')).values('day').annotate(total=Sum('montant')).order_by('day')
    
    # Conversion des mois et jours en objets datetime pour utilisation dans le formulaire
    mois_objets = []
    for item in bilan_par_mois:
        mois_objets.append(datetime(item['month'].year, item['month'].month, 1))
    
    jours_objets = []
    for item in bilan_par_jour:
        jours_objets.append(item['day'])
    
    context = {
        'bilan_par_annee': bilan_par_annee,
        'bilan_par_mois': bilan_par_mois,
        'bilan_par_jour': bilan_par_jour,
        'annee': annee,
        'mois': mois,
        'date': date,
        'mois_objets': mois_objets,
        'jours_objets': jours_objets,
    }
    
    return render(request, 'bilan.html', context)
