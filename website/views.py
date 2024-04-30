from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm,ProductForm
from .models import Record, Test, LabDeposit
from django.shortcuts import get_object_or_404, redirect
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import io
from django.http import HttpResponse


from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import ParagraphStyle
from django.http import HttpResponse
import io
from reportlab.lib.enums import TA_CENTER, TA_RIGHT


lab_choices = [
    ('lab1', 'Lab 1'),
    ('lab2', 'Lab 2'),
    ('lab3', 'Lab 3'),
    ('lab4', 'Lab 4'),
    ('lab5', 'Lab 5')
]

def generate_pdf(request, month, lab):
    # Parse the month parameter to extract year and month
    year, month = map(int, month.split('-'))

    # Filter records for the selected month
    records = Record.objects.filter(created_at__year=year, created_at__month=month, lab=lab)

    # Create a buffer to store PDF data
    buffer = io.BytesIO()

    # Create a PDF document
    pdf = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    # Title with Lab Name
    title_text = f"Records for {lab} - {year}-{month}"
    title_style = ParagraphStyle(name='TitleStyle', fontSize=14, alignment=TA_CENTER, spaceAfter=10)
    title = Paragraph(title_text, title_style)
    elements.append(title)

    # Define table headers and data
    table_data = [['Name' 'Lab', 'Total Price']]
    total_price = 0
    for record in records:
        table_data.append([
            f"{record.first_name}",
            
            record.lab,
            record.total_price
            
        ])
        total_price += record.total_price

    # Create a Table object
    table = Table(table_data)

    # Define style for table cells
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ])

    # Apply style to the table
    table.setStyle(style)

    # Add the table to the PDF document
    elements.append(table)

    # Add Total Price
    total_text = f"Total : {total_price}"
    total_style = ParagraphStyle(name='TotalStyle', fontSize=12, alignment=TA_RIGHT)
    total = Paragraph(total_text, total_style)
    elements.append(total)

    # Build the PDF
    pdf.build(elements)

    # Close the PDF buffer
    buffer.seek(0)

    # Return the PDF as a response
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=records_{year}-{month}.pdf'
    return response




def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_product')  # Redirect to a page displaying all products
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def product_list(request):
    products = Test.objects.all()
    return render(request, 'product_list.html', {'products': products})

def pay_option(request, record_id):
    record = get_object_or_404(Record, pk=record_id)
    record.paid = 'paid'
    record.save()
    return redirect('home')  
def pay_option2(request, record_id):
    record = get_object_or_404(Record, pk=record_id)
    record.paid = 'paid'
    record.save()
    return redirect('udhaar')  

def udhaar(request):
	records = Record.objects.all()
	return render(request, 'udhaar.html', {'records':records})
	

def home(request):
	records = Record.objects.filter(lab="Ashish_Lab")
	
	total_credited=0
	total_debited=0
	for record in records:
		total_credited += record.total_price
		if record.paid=="paid":
			total_debited+= record.total_price	
	
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('home')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('home')
	else:
		return render(request, 'home.html', {'records':records, 'credited':total_credited, 'debited':total_debited})



def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})



def customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')



def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')


def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')


def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
	
def labs_list(request):
    if request.method == 'POST':
          label = request.POST.get('label')
          form = AddRecordForm()
          form.add_lab_choice('label', 'label')
          print(label)
          

    labs = Record.objects.values_list('lab', flat=True).distinct()
    return render(request, 'labs_list.html', {'labs': labs})

def lab_records(request, lab):
    records = Record.objects.filter(lab=lab)
    
	
    total_price = 0
    
    for record in records:
        
        total_price += record.total_price
			   
    
    if lab == 'lab3':
		
        deposited =0
        for record in records:
              if record.paid == 'paid':
                    deposited += record.total_price
	
        return render(request, 'lab_records.html', {'records': records, 'lab': lab, 'deposit': deposited, "credited": total_price})
	
    try:
        lab_deposit = LabDeposit.objects.get(lab=lab)
    except LabDeposit.DoesNotExist:
        lab_deposit= None

    return render(request, 'lab_records.html', {'records': records, 'lab': lab, 'deposit': lab_deposit.deposit if lab_deposit else 0, "credited": total_price})





def add_deposit(request, lab):
    
	
    
    if request.method == 'POST':
        deposit_amount = request.POST.get('deposit')
        if deposit_amount:
            try:
                lab_deposit = LabDeposit.objects.get(lab=lab)
                lab_deposit.deposit += int(deposit_amount)
                lab_deposit.save()
            except LabDeposit.DoesNotExist:
                # If LabDeposit object doesn't exist, create a new one
                LabDeposit.objects.create(lab=lab, deposit=int(deposit_amount))
			    
				
            #return redirect('lab_records')
	
        lab_deposit = None
            # Try to retrieve LabDeposit object for the given lab
        try:
            lab_deposit = LabDeposit.objects.get(lab=lab)
        except LabDeposit.DoesNotExist:
            pass 

            
        records = Record.objects.filter(lab=lab)
		
		
        total_price = 0
    
        for record in records:
		   
           if record.paid=='udhaar':
               total_price += record.total_price
		   
        if total_price==lab_deposit.deposit:
		    
            Record.objects.filter(lab=lab).update(paid='paid')
			
            lab_deposit = LabDeposit.objects.get(lab=lab)
            lab_deposit.deposit = 0
            lab_deposit.save()
			
            total_price=0
			
            records = Record.objects.filter(lab=lab)
			
        
        
        return render(request, 'lab_records.html', {'records': records, 'lab': lab, 'deposit': lab_deposit.deposit if lab_deposit else 0, "credited": total_price})
    


def search_records(request):
    query = request.GET.get('query')

    if query:
        records = Record.objects.filter(first_name__icontains=query)
    else:
        records = Record.objects.all()

    return render(request, 'home.html', {'records': records})