import pandas as pd
from django.shortcuts import render
from store.models import Product
from django.core.files.storage import FileSystemStorage
from tablib import Dataset

def importExcel(request):
    uploaded_file_url = None

    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        if filename.endswith('.xlsx'):
            empexceldata = pd.read_excel(filename)
        elif filename.endswith('.csv'):
            empexceldata = pd.read_csv(filename)
        else:
            # Handle unsupported file formats here
            pass

        for row in empexceldata.itertuples():
            try:
                obj = Product.objects.create(
                    
                    item=row.item,
                    quantity=row.quantity,
                    amount=row.amount,
                    date=row.date
                )
                obj.save()
            except ValueError as e:
                # Handle the error gracefully, e.g., log it or skip the problematic row
                print(f"Error importing row: {e}")

    return render(request, 'hello.html', {'uploaded_file_url': uploaded_file_url})
