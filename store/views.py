from django.http import HttpResponse
import pandas as pd
import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from store.form import ProductForm
from store.models import Product, Customer
from django.core.files.storage import FileSystemStorage
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy




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
            
            item=row.item if not pd.isna(row.item) else 'none'
            quantity=row.quantity if not pd.isna(row.quantity) else 0
                
            try:
                amount=float(row.amount)

            except (ValueError, TypeError):
                    amount=0.0
              
            date=row.date if not pd.isna(row.date) else '2023-01-01'
                
            try:
                obj = Product.objects.create(
                    
                    item=item,
                    quantity=quantity,
                    amount=amount,
                    date=date 
                )
                obj.save()
            except ValueError as e:
                # Handle the error gracefully, e.g., log it or skip the problematic row
                print(f"Error importing row: {e}")

    return render(request, 'hello.html', {'uploaded_file_url': uploaded_file_url})



def displayTable(request):
   if request.method == 'GET':
    tablelist=Product.objects.all()
    context = {'tablelist': tablelist}
   return render(request, 'form.html', context)


def edit_table(request, id):
  product=get_object_or_404(Product, id=id)
  form=ProductForm(instance=product)

  if request.method =='POST':
    form=ProductForm(request.POST, instance=product)

    if form.is_valid():
      form.save()
      return redirect('table_list')
      
    else:
      form=ProductForm(instance=product)
  return render(request, 'edit.html', {'form': form, 'product': product})


def Delete_table(request, id):
  product=get_object_or_404(Product, id=id)
  product.delete()
  return redirect('table_list')

  
import csv
from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer

def retrieve_data(request):
    if request.method == 'GET':
        date_filter = request.GET.get('date_filter', None)  # Get the date parameter from the request
        data = Customer.objects.all()

        if date_filter:
            # If a date filter is provided, filter the data based on the date
            data = data.filter(date=date_filter)

        context = {'data': data}

        if 'export_csv' in request.GET:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="Customer_{date_filter}.csv"'

            writer = csv.writer(response)
            writer.writerow(['id', 'first_name', 'last_name', 'email', 'gender', 'date'])

            for item in data:
                writer.writerow([item.id, item.first_name, item.last_name, item.email, item.gender, item.date])

            return response

    return render(request, 'retrieve.html', context)

  

 