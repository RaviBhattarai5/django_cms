from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ImportTest
from .resources import ImportTestResource
from .forms import ImportTestForm
from tablib import Dataset

def import_excel(request):
    if request.method == 'POST':
        form = ImportTestForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']
            
            if not excel_file.name.endswith('.xlsx'):
                messages.error(request, 'Wrong file format. Please upload an Excel file.')
                return redirect('import_excel')

            import_test_resource = ImportTestResource()
            dataset = Dataset()
            imported_data = dataset.load(excel_file.read(), format='xlsx')

            print(imported_data)
            for row in imported_data.dict:
                first_name = row.get('first_name') 
                last_name = row.get('last_name')
                
                print(row)
            
            result = import_test_resource.import_data(dataset, dry_run=True)  # Test the data import
            if not result.has_errors():
                import_test_resource.import_data(dataset, dry_run=False)  # Actually import now
                messages.success(request, 'Excel file has been imported successfully.')
            else:
                messages.error(request, 'There were errors importing the file.')
                messages.error(request, result.row_errors)
                # Optionally, you can iterate through result.row_errors() to get specific error messages

            return redirect('import_excel')
    else:
        form = ImportTestForm()
    
    return render(request, 'import_excel.html', {'form': form})