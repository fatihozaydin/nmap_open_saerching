import os

def nmap_hello():
    print("""

    ************************************************
          
            Welcome To Nmap Open Searching
          
 
                    Do you Want It
          
                    1-        Yes
          
                    2-        No

    ************************************************
          
        """)
    
    
    
    
    processNo = input(" Please Enter Process Number: ")
    ip = input(" Please Enter The IP: ")

    if(processNo=="1"):
        os.system("nmap -Pn --script vuln "+ip)
    elif(processNo=="2"):
        exit



nmap_hello()