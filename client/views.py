from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Client
from .forms import ClientForm



# === BACKEND FORM SUBMIT ANS DISPLAY ===|
def index(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClientForm()
    
    clients = Client.objects.all()
    return render(request, 'index.html', {'form': form, 'clients': clients})


# === WASH COUT ===|
def wash_count(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    client.washcount += 1
    client.save()
    # IF 5 WASH FOR YOU DISPLYING MESSAGE
    if client.washcount % 5 == 0:
        messages.success(request, f"تهانينا! الغسلة رقم {client.washcount} للعميل  {client.name} مجاناً")
    
    return redirect('index')


# === WASH COUT RESET ===|
def reset_wash_count(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    client.washcount = 0
    client.save()
    return redirect('index')




###### ######      ###### ######        ###### ##################    
###### ######      ###### ######        ######             ######
######       ######       ######        ######             ######
######       ######       ######        ######
######                    ######        ######      ###### ######
######                    ######        ######      ###### ######
######                    ######        ######             ######
######                    ######        ###### ##################



