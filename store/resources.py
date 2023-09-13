from import_export import resources
from .models import Product


class ProductRessources(resources.ModelResource):

    class Meta:
        model = Product
        





