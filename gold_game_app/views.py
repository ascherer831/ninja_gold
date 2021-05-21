from django.shortcuts import render, redirect
import random
# Create your views here.

def index(request):
    if 'activity' not in request.session:
        request.session['activity'] = []
    if 'your_gold' not in request.session:
        request.session['your_gold'] = 0
    return render(request, 'index.html')
    

def get_gold(request):
    farm_gold = random.randint(10,20)
    cave_gold = random.randint(5,10)
    house_gold = random.randint(2,5)
    casino_gold = random.randint(-50,50)

    if request.POST['location'] == 'farm':
        request.session['your_gold'] += farm_gold
        request.session['activity'].insert(0,f"Earned {farm_gold} DOGE COIN from the Farm")

    elif request.POST['location'] == 'cave':
        request.session['your_gold'] += cave_gold
        request.session['activity'].insert(0,f"Earned {cave_gold} DOGE COIN from the Cave")

    elif request.POST['location'] == 'house':
        request.session['your_gold'] += house_gold
        request.session['activity'].insert(0,f"Earned {house_gold} DOGE COIN from the House")

    elif request.POST['location'] == 'casino':
        request.session['your_gold'] += casino_gold
        if casino_gold > 0:
            request.session['activity'].insert(0,f"Entered a Casino and won {casino_gold} DOGE COIN")
        else:
            request.session['activity'].insert(0,f"Entered a Casino and lost {casino_gold*-1} DOGE COIN... Ouch...")
            if request.session['your_gold'] < 0:
                request.session['activity'].insert(0,'Your coin account is negative! Better make some coin quick. The Casino is looking for you!')

    return redirect('/')

def restart(request):
    request.session.flush()
    return redirect('/')
