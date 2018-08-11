from rest_framework import serializers
from apps.RobotManager.models import Project,Module,Cases,\
    Suites,Keyword,UserKeywords,Steps,Resource,CasesStep
from apps.users.models import UserProfile





class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields='__all__'


class ModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model=Module
        fields='__all__'


class CasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cases
        fields = '__all__'


class SuitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suites
        fields = '__all__'


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'

class UserKeywordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserKeywords
        fields = '__all__'

class StepswordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Steps
        fields = '__all__'

class ResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'

class CasesStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasesStep
        fields = '__all__'