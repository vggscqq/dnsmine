import dns.resolver, dns.reversename
import re
import sre_yield
import time



# https://www.regextester.com/
# https://habr.com/ru/post/567106/
knownIP = "[1-9]1\.[1-9]1\.2\d5\.1\d{2}" # IP: *1.*1.2*5*.1**
knownDomain = "si[a-z]+\.ru" # si*.ru

reDomain = re.compile(knownDomain)
reIP = re.compile(knownIP)

nameservers=["8.8.8.8", "8.8.4.4", "1.1.1.1"]

a = 0 # counter
resolver = dns.resolver.Resolver()
resolver.nameservers = nameservers

for aDomain in sre_yield.AllStrings(knownDomain): # regexp generator for all domains
    #print(aDomain)
    a+=1
    try:
        answer = resolver.resolve(aDomain , "A")
        #print(answer)
        for anIP in list(answer): # checking all A entries
            if(reIP.match(str(anIP))): # if A entry contains mathing IP
                print("FOUND!#{} Checking: {} Answer: {} FOUND!".format(a, aDomain, list(answer)))
                with open("found.txt", "a") as f: # adding "good" IP to file
                    f.write("Domain: {} IP: {}\n".format(aDomain, anIP))
            #break
        print("#{} Checking: {} Answer: {}".format(a, aDomain, list(answer)))
    except dns.exception.Timeout: # in case DNS serer failed to answer in right time try *one* more time
        try:
            print("Sleep for 2 seconds, due to timeout error")
            time.sleep(2)
            answer = resolver.resolve(aDomain , "A")
            #print(answer)
            for anIP in list(answer):
                if(reIP.match(str(anIP))):
                    print("FOUND!#{} Checking: {} Answer: {} FOUND!".format(a, aDomain, list(answer)))
                    with open("found.txt", "a") as f:
                        f.write("Domain: {} IP: {}\n".format(aDomain, anIP))
                #break
            print("#{} Checking: {} Answer: {}".format(a, aDomain, list(answer)))
        except Exception:
            pass
    except ( # in case domain not exist
        dns.resolver.NXDOMAIN,
        dns.resolver.NoNameservers,
        dns.resolver.NoAnswer):
        print("#{} Checking: {} Answer: Do not exist".format(a, aDomain))
    #print(a)
