from rest_framework.generics import RetrieveAPIView

from .models import TitleBasic
from .serializers import *


class TitleDetailView(RetrieveAPIView):
    lookup_field = 'tconst'
    queryset = TitleBasic.objects.all()
    # serializer_class = TitleBasicSerializer
    serializer_class = TitleSerializer
