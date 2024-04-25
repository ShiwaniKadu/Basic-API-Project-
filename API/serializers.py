from rest_framework import serializers
from API.models import Company

class CompanySerilizers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        field = "__all__"