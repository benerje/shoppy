import django_filters
from django_filters import CharFilter

from .models import *


class OrderFilter(django_filters.FilterSet):

    class Meta:
        model = Ordercheckout
        fields = ['username', 'email']
