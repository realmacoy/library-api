from django.urls import path, re_path
from .views import TitleDetailView

urlpatterns = [
    re_path(r'^titles/(?P<tconst>tt\d+)/$', TitleDetailView.as_view(), name='title_detail')
]