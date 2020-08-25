from django.urls import path, include
from django.views.generic import TemplateView
from demo import views as demo_views
from django.urls import re_path, path

app_name='demo'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('template/', TemplateView.as_view(template_name='test2.html')),
    path('test/', demo_views.test, name="test"),
    path('check_processing/', demo_views.processing, name="processing"),
    re_path(r'^$', demo_views.myModel_asJson, name="my_ajax_url")

]
