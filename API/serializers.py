from rest_framework import serializers
from API.models import Company,Employee

class CompanySerilizers(serializers.ModelSerializer):
    class Meta:
        company_id = serializers.ReadOnlyField()
        model = Company
        fields = "__all__"


class EmployeeSerializers(serializers.HyperlinkedModelSerializer):
    ide=serializers.ReadOnlyField()

    class Meta:
        model=Employee
        fields = "__all__"
