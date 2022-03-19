
from django.shortcuts import redirect, render,get_object_or_404
import threading
import alert
import alert.sniffer as sniffer
import csv

from alert.models import CapturedPackets
from .models import CapturedPackets

# Create your views here.


def startSniffing():
    reader = csv.reader(open('alert/rules.csv', mode='r'))
    rules = list(reader)

    def check_rules(p):
        for i in range(len(rules)):
            if rules[i][0] in str(p).lower():
                x = CapturedPackets()
                x.title = rules[i][1]
                x.p_content = str(p)
                x.save()
                #print(rules[i][1])

    def capture(cap):
        for p in cap:
            # p.pretty_print()
            check_rules(p)

    def main():

        cap = sniffer._sniff(continuous=True)

        capture(cap)

    main()


t1 = threading.Thread(target=startSniffing)
t1.start()


def index(request):

    cap_packs = CapturedPackets.objects.all()

    return render(request, "index.html", {"cap_packs":cap_packs})

def delete(request,id):
    packet = get_object_or_404(CapturedPackets,id = id)

    packet.delete()
    return redirect("/")