from tastypie.resources import ModelResource, ALL
from tastypie.authorization import Authorization
from tastypie import fields
from API.models import Investment, Updates


class InvestmentResource(ModelResource):

    class Meta:
        queryset = Investment.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post']
        filtering = {
            'date': ALL,
        }
        resource_name = 'investment'
        authorization = Authorization()
        fields = ['company', 'quantity', 'cost', 'date']
        excludes = ['id']


class UpdatesResource(ModelResource):

    investment = fields.ForeignKey(InvestmentResource, 'investment')

    class Meta:
        queryset = Updates.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post']
        filtering = {
            'date': ALL,
            'date_entered': ('lte',),
            'investment_id': ALL
        }
        resource_name = 'updates'
        authorization = Authorization()
        fields = ['quantity', 'cost', 'investment', 'date']
        excludes = ['id']

#Finally got POST call to work to create updates
# {
#     "quantity" : 5,
#     "cost" : 10,
#     "investment" : "/api/investment/3/"
# }
