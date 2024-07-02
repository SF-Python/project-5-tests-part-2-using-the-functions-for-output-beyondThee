#Mario Remirez (beyondThee)
#COP2002.0M1
#7/2/2024
#project5 part 2
#teaches user what protocol is assigned to what port number

import random

# Define the dictionary of port numbers and the corresponding protocols
portProtocolDict = {
    20: 'FTP',
    21: 'FTP',
    22: 'SSH',
    23: 'TELNET',
    25: 'SMTP',
    53: 'DNS',
    67: 'DHCP',
    68: 'DHCP',
    80: 'HTTP',
    110: 'POP3',
    137: 'NetBIOS',
    139: 'NetBIOS',
    143: 'IMAP',
    161: 'SNMP',
    162: 'SNMP',
    389: 'LDAP',
    443: 'HTTPS',
    445: 'SMB',
    3389: 'RDP',
}

#main menu user options 
def mainMenu():
    print("Main Menu:")
    print("1. Given a port number, identify the PROTOCOL (use abbreviation).")
    print("2. Given a port protocol, identify a port NUMBER.")
    print("3. Exit")

#connects ports to protocols
def numToName():
    while True:
        port = random.choice(list(portProtocolDict.keys()))
        print(f"\nIdentify the PROTOCOL for port number {port} (M=Main Menu)")
        getInput = input("Your answer: ").strip().upper()
        if getInput == 'M':
            return
        elif getInput == '':
            continue
        elif getInput == portProtocolDict[port]:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {portProtocolDict[port]}.")
            
#connects protocols to ports
def nameToNum():
    while True:
        protocol = random.choice(list(portProtocolDict.values()))
        print(f"\nIdentify the port NUMBER for protocol {protocol} (M=Main Menu)")
        getInput = input("Your answer: ").strip()
        if getInput == 'M':
            return
        elif getInput == '':
            continue
        try:
            if int(getInput) in [port for port, prot in portProtocolDict.items() if prot == protocol]:
                print("Correct!")
            else:
                print(f"Incorrect. The correct answer is {', '.join([str(port) for port, prot in portProtocolDict.items() if prot == protocol])}.")
        except ValueError:
            print("Please enter a valid number.")

#main menu choices
while True:
    mainMenu()
    choice = input("Please choose an option (1-3): ").strip()
    
    if choice == '1':
        print("\nYou chose: Given a port number, identify the PROTOCOL (use abbreviation).")
        numToName()
    elif choice == '2':
        print("\nYou chose: Given a port protocol, identify the port NUMBER.")
        nameToNum()
    elif choice == '3':
        print("Program Complete.  I hope this has helped in studying for the CompTIA A+ certification.")
        break
    else:
        print("Invalid choice. Please choose again.")
