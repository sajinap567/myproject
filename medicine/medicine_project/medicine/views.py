# medicalshop/views.py
from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from .models import Medicine
from django.db.models import Q
from .forms import MedicineForm
from django.contrib import messages

def medicine_list(request):
    query = request.GET.get('q')  # Get search term from the URL
    medicine_list = Medicine.objects.all().order_by('id')

    # If user searched for something
    if query:
        medicine_list = medicine_list.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    paginator = Paginator(medicine_list, 10)  # Show 10 medicines per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query,  # So we can keep the search term in the form
    }
    return render(request, 'medicine/medicine_list.html', context)


def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Medicine added successfully!")  # ✅ Message added
            return redirect('medicine_list')  # Redirect to medicine list after saving
        else:
            messages.error(request, "❌ Please correct the errors below.")
    else:
        form = MedicineForm()

    return render(request, 'medicine/add_medicine.html', {'form': form})

def delete_medicine(request, pk):
    medicine = Medicine.objects.get(pk=pk)
    medicine.delete()
    messages.success(request, f"✅ Medicine '{medicine.name}' deleted successfully.")
    return redirect('medicine_list')
