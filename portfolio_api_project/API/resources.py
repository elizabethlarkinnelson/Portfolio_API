from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from API.models import Investment


class InvestmentResource(ModelResource):
    class Meta:
        queryset = Investment.objects.all()
        resource_name = 'investment'
        authorization = Authorization()
        fields = ['company', 'quantity', 'paid']
