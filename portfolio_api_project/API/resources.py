from tastypie.resources import ModelResource, ALL
from tastypie.authorization import Authorization
from API.models import Investment


class InvestmentResource(ModelResource):
    class Meta:
        queryset = Investment.objects.all()
        filtering = {
            'date': ALL,
        }
        resource_name = 'investment'
        authorization = Authorization()
        fields = ['company', 'quantity', 'cost']
