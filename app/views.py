from django.shortcuts import render
from .models import Panel
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import json
from django.http import StreamingHttpResponse
import redis
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver



def show_data(request):
    data = Panel.objects.filter().order_by("-date")
    return render(request, 'app/home.html', {"data": data})

def staff_report(request):
    total_produced_energy = 0
    total_consumed_energy = 0
    tot_report = Panel.objects.filter().order_by("-date")
    for e in tot_report:
        total_produced_energy = total_produced_energy + e.produced_energy
        total_consumed_energy = total_consumed_energy + e.consumed_energy
    data = {
        "total_produced": total_produced_energy,
        "total_consumed": total_consumed_energy
    }
    return render(request, "app/total.html", data)

@csrf_exempt
def record_data(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body)
        r = Panel()
        r.date = timezone.now()
        r.consumed_energy = received_json_data['consumed_energy_in_watt']
        r.produced_energy = received_json_data['produced_energy_in_watt']
        r.writeOnChain()
        r.publish()
        return StreamingHttpResponse('Json Data were sent correctly to the webapp')
    else:
        return StreamingHttpResponse('Endpoint Page')


client = redis.StrictRedis(host='127.0.0.1', port=6379, password='',db=0, decode_responses=True)

@receiver(user_logged_in)
def ip_check(sender, user, request, **kwargs):
    diff_ip = False
    username = request.user.username
    last_ip = client.get(username)
    current_ip = request.META['REMOTE_ADDR']
    if last_ip is None:
        client.set(username, current_ip)
    elif current_ip != last_ip:
        client.set(username, current_ip)
        diff_ip = True
    print(f'ip_check: is different?: {diff_ip}')
    print(f"current: {current_ip}, last: {last_ip}")
    return diff_ip
