from django.core.management.base import BaseCommand
from myRevendeurBackOffice.models import InfoProduct
from myRevendeurBackOffice.views import putOnSale
from myRevendeurBackOffice.views import removesale
from myRevendeurBackOffice.models import InfoProduct
class Command(BaseCommand):
    
    help = 'Update product sales automatically'

    def handle(self, *args, **kwargs):
        put_OnSale = putOnSale()
        remove_sale = removesale()
        products = InfoProduct.objects.all()
        for product in products:
            if product.quantityInStock > 16:
                if 16 <= product.quantityInStock <= 64:
                    put_OnSale.get_object(tig_id=product.tig_id, newPrice=80)
                else:
                    put_OnSale.get_object(tig_id=product.tig_id, newPrice=50)
            else:
                remove_sale.get_object(tig_id=product.tig_id)

        self.stdout.write(self.style.SUCCESS('Successfully updated product sales'))
