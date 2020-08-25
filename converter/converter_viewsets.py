from rest_framework.viewsets import ModelViewSet, ViewSet
from.models import ConverterModel
from .serializers import DataTableSerializer

"""class FileViewSet(ModelViewSet):
    serializer_class = DataTableSerializer
    queryset = ConverterModel.objects.all().order_by('-updated_at')

    filter_backends = (drf.DjangoFilterBackend, SearchFilter)
    filter_fields = ('status', 'created_at', 'updated_at')
    filterset_fields = {
       'title': ['icontains', 'istartswith'],
       'full_name': ['icontains', 'istartswith'],
       'created_at': ['lt', 'lte', 'gt', 'gte'],
       'updated_at': ['lt', 'lte', 'gt', 'gte'],
       'status': ['iexact'],
   }
    ordering = ('id', 'created_at', 'updated_at')
    search_fields = ('title', 'mobile_number', 'account_no')

    def list(self, request, *args, **kwargs):
        custom_data = {
            'recordsTotal': len(self.get_queryset()),
            'recordsFiltered': len(self.get_queryset()),
            'data': DocumentSerializer(self.get_queryset(),many=True).data,  # this is the default result you are getting today
        }
        return Response(custom_data)
"""

class AllMediaViewSet(ModelViewSet):
    queryset = ConverterModel.objects.all().order_by('-updated_at')
    serializer_class = DataTableSerializer

class ProcessedMediaViewSet(ModelViewSet):
    queryset = ConverterModel.objects.filter(status='done')
    serializer_class = DataTableSerializer

class FailedMediaViewSet(ModelViewSet):
    queryset = ConverterModel.objects.filter(status='error')
    serializer_class = DataTableSerializer

class WaitingMediaViewSet(ModelViewSet):
    queryset = ConverterModel.objects.filter(status='waiting')
    serializer_class = DataTableSerializer

class ProcessingMediaViewSet(ModelViewSet):
    queryset = ConverterModel.objects.filter(status='processing')
    serializer_class = DataTableSerializer

class UnavailableMediaViewSet(ModelViewSet):
    queryset = ConverterModel.objects.filter(status='unavailable')
    serializer_class = DataTableSerializer

