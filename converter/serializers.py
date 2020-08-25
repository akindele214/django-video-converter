from rest_framework import serializers 
from .models import ConverterModel

class ConverterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConverterModel
        fields = "__all__"

class DataTableSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    DT_RowId = serializers.SerializerMethodField()
    DT_RowAttr = serializers.SerializerMethodField()
    name = serializers.CharField()
    media = serializers.CharField()
    output = serializers.CharField()
    status = serializers.CharField()
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    def get_DT_RowId(self, sample):
        return 'row_%d' % sample.pk

    def get_DT_RowAttr(self, sample):
        return {'data-pk': sample.pk}


    class Meta:
        model = ConverterModel
        fields = (
             'DT_RowId', 'DT_RowAttr', 'id', 'name', 'media', 'output',
             'updated_at', 'status',
        )
    