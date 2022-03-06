
from django.shortcuts import render
import threading
import alert.sniffer as sniffer
import csv

from alert.models import CapturedPackets

# Create your views here.


def startSniffing():
    #database_connect = sqlite3.connect("db.sqlite3")
    #cursor = database_connect.cursor()
    #cursor.execute("INSERT INTO alert_capturedpackets (p_content) VALUES ('asd')")

    #x = CapturedPackets()
    #x.p_content = 'This is the content'
    # x.save()
    reader = csv.reader(open('alert/rules.csv', mode='r'))
    rules = list(reader)

    def check_rules(p):
        for i in range(len(rules)):
            if rules[i][0] in str(p).lower():
                x = CapturedPackets()
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
    return render(request, "index.html")
