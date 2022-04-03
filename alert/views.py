

from struct import pack
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Count
import threading

from alert.models import ArchivedPacket, CapturedPacket
from alert.startSniff import startSniffing

from .filters import PacketFilter

# Create your views here.


t1 = threading.Thread(target=startSniffing)
t1.start()


def index(request):
    return render(request, "index.html")


def alerts(request):

    cap_packsAll = CapturedPacket.objects.all().order_by("time")

    cap_packs = (CapturedPacket.objects
                 .values('title','rule')
                 .annotate(dcount=Count('title'))
                 .order_by()
                 )
    print(cap_packs)

    return render(request , "alerts.html", {"cap_packs": cap_packs, "cap_packsAll": cap_packsAll})

def archive(request):

    


    cap_packs = ArchivedPacket.objects.all()

    myFilter = PacketFilter(request.GET , queryset=cap_packs)
    
    cap_packs = myFilter.qs

    return render(request, "archive.html", {"cap_packs": cap_packs, "cap_packsAll": cap_packs, "myFilter": myFilter})


def delete(request, id):
    try:
        packet = get_object_or_404(CapturedPacket, id=id)
        y = ArchivedPacket()
        y.time = packet.time
        y.title = packet.title
        y.p_content = packet.p_content
        y.rule = packet.rule
        y.source = packet.source
        y.dest = packet.dest
        y.s_port = packet.s_port
        y.d_port = packet.d_port
        y.protocol = packet.protocol
        y.save()
        packet.delete()
        print("Record deleted successfully!")
        return redirect("/alerts")
    except:
        print("Record doesn't exists")
        return redirect("/alerts")
