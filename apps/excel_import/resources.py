from import_export import resources
from .models import ImportTest

class ImportTestResource(resources.ModelResource):
    class Meta:
        model = ImportTest
        import_id_fields = ['email']  # for checking duplicate field 
        fields = ('first_name','last_name', 'email', 'age')