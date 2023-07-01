from rest_framework import routers
from django.urls import path, include
from .views import UserViewSet, CompteViewSet, CategorieDepenseViewSet, RevenuViewSet, DepenseViewSet, TransactionViewSet,\
    BilanView, CategorieRevenuViewSet, DeviseViewSet, ParametreViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'comptes', CompteViewSet)
router.register(r'categories-depense', CategorieDepenseViewSet)
router.register(r'revenus', RevenuViewSet)
router.register(r'depenses', DepenseViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'categories-revenus', CategorieRevenuViewSet)
router.register(r'devises', DeviseViewSet)
router.register(r'parametres', ParametreViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('bilan/', BilanView.as_view(), name='bilan'),
]

