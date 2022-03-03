import sniffer as sniffer
import csv
import os

reader = csv.reader(open('rules.csv', mode='r'))
rules = list(reader)


def clear():

    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')
        
        
def check_rules(p):
    for i in range(len(rules)):
    	
    	if rules[i][0] in str(p).lower():
    	    #print(p.pretty_print())
    	    print(rules[i][1])

def capture(cap):
    for p in cap:
        #p.pretty_print()
        check_rules(p)
    
    

def main():
    """
    Main driver for the IDS

    """
    
    
    cap = sniffer._sniff(continuous=True)

    print("IDS Successfully Starded!")
    
    capture(cap)
    

            
main()
