from rest_framework.serializers import ModelSerializer
from myRevendeurBackOffice.models import InfoProduct
from myRevendeurBackOffice.models import ProduitPoisson

class InfoProductSerializer(ModelSerializer):
    class Meta:
        model = InfoProduct
        fields = ('id', 'tig_id', 'name', 'category', 'price', 'unit', 'availability', 'sale', 'discount', 'comments', 'owner', 'quantityInStock')
class ProduitPoissonSerializer(ModelSerializer):
    class Meta:
        model = ProduitPoisson
        fields = ('id', 'tigID')