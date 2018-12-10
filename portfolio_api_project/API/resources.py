from tastypie.resources import ModelResource, ALL
from tastypie.authorization import Authorization
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
        fields = ['company', 'quantity', 'cost']
        excludes = ['id', 'date']


class UpdateResource(ModelResource):
    class Meta:
        queryset = Updates.objects.all()
        list_allowed_methods = ['get', 'put']
        detail_allowed_methods = ['get', 'put']
        filtering = {
            'date': ALL
        }
        fields = ['company', 'quantity', 'cost']
        excludes = ['id', 'date']
        