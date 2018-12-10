from tastypie.resources import ModelResource
from API.models import Investment


class InvestmentResource(ModelResource):
    class Meta:
        queryset = Investment.objects.all()
        resource_name = 'investment'
