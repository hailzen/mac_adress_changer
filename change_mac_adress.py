import os,re,optparse,subprocess
def get_mac_adress(interface):
    output = subprocess.check_output(['ifconfig',interface])
    mac_adress = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(output))
    return mac_adress[0]
def get_input():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest='interface',help='Interface to cahnge mac adress')
    parser.add_option('-m','--mac',dest="mac",help="Mac adress that wille be changed of interface")
    (options,args) = parser.parse_args()
    if options.interface is not None and options.mac is not None:
        result=[options.interface,options.mac]
    elif options.interface is not None and options.mac is None:
        mac = input(f'Enter mac adress that will be assigned to {options.interface} : ')
        result=[options.interface,mac]
    elif options.interface is None and options.mac is not None:
        interface = input(f'Enter interface that will be assigned to {options.mac} : ')
        result=[interface,options.mac]
    else:
        interface = input(f'Enter interface which mac adress will be changed : ')
        mac = input(f'Enter mac adress that will be changed of interface {interface} : ')
        result=[interface,mac]
    return result
def cahnge_mac_adress(interface,mac):
    os.system("sudo service NetworkManager stop")
    os.system(f"sudo ifconfig {interface} down")
    os.system(f"sudo ifconfig {interface} hw ether {mac}")
    os.system(f"sudo ifconfig {interface} up")
    os.system("sudo service NetworkManager start")
inputed = get_input()
interface,mac=inputed[0],inputed[1]
mac_adress_before_changing = get_mac_adress(interface)
cahnge_mac_adress(interface,mac)
mac_adress_after_changing = get_mac_adress(interface)
if mac_adress_after_changing != mac_adress_before_changing:
    print('')
    print(f"Mac adress has beeen sucessfullly changed from {mac_adress_before_changing} to {mac_adress_after_changing} ")
else :
    print('')
    print("Error ")