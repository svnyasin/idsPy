
from datetime import datetime

from django.utils import timezone
import alert.sniffer as sniffer
import csv
from alert.models import CapturedPacket



def startSniffing():
    reader = csv.reader(open('alert/rules.csv', mode='r'))
    rules = list(reader)

    def check_rules(p):
        
        for i in range(len(rules)-1):
            if rules[i][0] in str(p).lower():
                x = CapturedPacket()
                x.time = timezone.now()
                x.title = rules[i][1]
                x.rule = rules[i][0]
                x.p_content = str(p)
                x.source = p.ip.src
                x.dest = p.ip.dst
                if hasattr(p, 'tcp'):
                    x.s_port = p.tcp.srcport
                    x.d_port = p.tcp.dstport
                if hasattr(p, 'udp'):
                    x.s_port = p.udp.srcport
                    x.d_port = p.udp.dstport
                x.protocol = p.ip.proto
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


