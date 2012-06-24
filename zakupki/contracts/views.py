# Create your views here.
from django.views.generic import DetailView,ListView
from contracts.models import *


class ContractsListView(ListView):
    model = Contracts

class ContractsDetailView(DetailView):
    model = Contracts
    slug_field = 'contract_uid'

class ContractsSuppliersDetailView(DetailView):
    model = ContractsSuppliers
    slug_field = 'order_uid'

