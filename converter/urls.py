from django.urls import path, include
from django.views.generic import TemplateView
from converter import views as converter_view
from django.urls import re_path, path

app_name='converter'

urlpatterns = [
    path('home/', converter_view.home, name='converter-home'),
    path('analysis/', converter_view.file_analysis, name='analysis'),
    path('error/', converter_view.error_list, name='error'),
    path('file/<int:pk>/', converter_view.FileDetailView.as_view(), name="file_detail"),

    path('documents/', converter_view.AllMediaView.as_view(), name='all_document'),
    path('failed/', converter_view.FailedMediaView.as_view(), name='failed_document'),
    path('unavailable/', converter_view.UnavailableMediaView.as_view(), name='unavailable_document'),
    path('processed/', converter_view.ProcessedMediaView.as_view(), name='processed_document'),
    path('queued/', converter_view.QueuedMediaView.as_view(), name='queued_document'),
    path('processing/', converter_view.ProcessingMediaView.as_view(), name='processing_document'),
    
    path('new/', converter_view.AddFileView.as_view(), name='new'),
    path('status/', converter_view.status, name='status'),
    path('file_count/', converter_view.file_count, name='file_count'),
    path('convert/<int:pk>', converter_view.convert, name="start_convert")
    # path('get_id/', converter_view.send, name='sms'),
    # path('',converter_view.DocumentHomeView.as_view(), name='home'),
    # path('test/', demo_views.test, name="test"),
    # path('check_processing/', demo_views.processing, name="processing"),
    # re_path(r'^$', demo_views.myModel_asJson, name="my_ajax_url")

]
