from rest_framework.serializers import ModelSerializer
from mytig.models import ProduitEnPromotion
from mytig.models import ProduitAvailable
from mytig.models import ProduitPoisson

class ProduitEnPromotionSerializer(ModelSerializer):
    class Meta:
        model = ProduitEnPromotion
        fields = ('id', 'tigID')
class ProduitAvailableSerializer(ModelSerializer):
    class Meta:
        model = ProduitAvailable
        fields = ('id', 'tigID')

class ProduitPoissonSerializer(ModelSerializer):
    class Meta:
        model = ProduitPoisson
        fields = ('id', 'tigID')