import time
import network
import socket
import smartconfig
import ntptime

NETWORK_PROFILES = 'wifi.dat'
wlan_sta = network.WLAN(network.STA_IF)
isconnected=wlan_sta.isconnected

def do_connect(ssid, password,light=0):
    wlan_sta.active(True)
    connected=False
    if wlan_sta.isconnected():
        return None
    networks = wlan_sta.scan()
    AUTHMODE = {0: "open", 1: "WEP", 2: "WPA-PSK", 3: "WPA2-PSK", 4: "WPA/WPA2-PSK"}
    for wifiId, bssid, channel, rssi, authmode, hidden in sorted(networks, key=lambda x: x[3], reverse=True):
        wifiId = wifiId.decode('utf-8')
        encrypted = authmode > 0
        print("ssid: %s chan: %d rssi: %d authmode: %s" % (wifiId, channel, rssi, AUTHMODE.get(authmode, '?')))
        if encrypted:
            if wifiId == ssid:
                print('Trying to connect to %s...' % wifiId)
                wlan_sta.connect(wifiId, password)    
                looptime=0
                tmp=1
                while not wlan_sta.isconnected():
                    if light:
                        led(tmp+1)
                    tmp=-tmp
                    time.sleep(0.1)
                    looptime+=1
                    print('.', end='')
                    if looptime >200:
                        return False
                connected=True
                break
            else:
                print("skipping unknown encrypted network")
    if connected:
        print('\nConnected. Network config: ', wlan_sta.ifconfig())
    else:
        print('\nFailed. Not Connected to: ' + ssid)
    return connected


def read_profiles():
    with open(NETWORK_PROFILES) as f:
        lines = f.readlines()
    profiles = {}
    for line in lines:
        ssid, password = line.strip("\n").split(";")
    return [ssid,password]

def write_profiles(profiles):
    lines = []
    print(profiles)
    for ssid, password in profiles.items():
        lines.append("%s;%s\n" % (ssid, password))
    with open(NETWORK_PROFILES, "w") as f:
        f.write(''.join(lines))

def inet_pton(ip_str:str):
    '''convert ip address from string to bytes'''
    ip_bytes = b''
    ip_segs = ip_str.split('.')

    for seg in ip_segs:
        ip_bytes += int(seg).to_bytes(1, 'little')

    return ip_bytes

def send_ack(local_ip, local_mac):
    '''sent ack_done event to phone'''
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    data = smartconfig.info()[3].to_bytes(1, 'little') + local_mac
    port = 10000 # airkiss port

    if smartconfig.info()[2] == smartconfig.TYPE_ESPTOUCH:
        data += inet_pton(local_ip)
        port = 18266 # esptouch port

    print(
f"""- sending ack:
    type: {'esptouch' if smartconfig.info()[2] == smartconfig.TYPE_ESPTOUCH else 'airkiss'}
    port: {port}
    data: {data}
    length: {len(data)}
"""
    )

    for _ in range(20):
        time.sleep(0.1)
        try:
            udp.sendto(data, ('255.255.255.255', port))
        except OSError:
            machine.reset()
            pass
    print('- ack was sent')

def reconnect():
    profiles=read_profiles()
    do_connect(profiles[0],profiles[1])

def get_connection():
    global wlan_sta
    if wlan_sta.isconnected():
        return wlan_sta
    connected = False
    try:
        time.sleep(3)
        if wlan_sta.isconnected():
            return wlan_sta
        profiles=read_profiles()
        connected = do_connect(profiles[0],profiles[1])
    except OSError:
        wlan_sta = network.WLAN(network.STA_IF)
        wlan_sta.active(True)
        print('- start smartconfig...')
        smartconfig.start()
        print('- waiting for success...')
        tmp=1
        duty=0
        while not smartconfig.success():
            duty+=tmp
            led(1,duty=duty)
            if duty ==1023:
                tmp=-1
            if duty == 0:
                tmp=1
            time.sleep_ms(1)
        ssid, password, sc_type, token = smartconfig.info()
        print(smartconfig.info())
        connected=do_connect(ssid, password,1)
        if not connected :
            print('wrong password')
            machine.reset()
        print('- wifi connected')
        profiles = {}
        profiles[ssid] = password
        while wlan_sta.ifconfig()[0] == '0.0.0.0':
            time.sleep(0.5)
        print('- got ip')
        print(wlan_sta.ifconfig())
        send_ack(wlan_sta.ifconfig()[0], wlan_sta.config('mac'))
        connected=True
        write_profiles(profiles)
    return wlan_sta if connected else None
def sync_time():
    try:
        ntptime.settime()
    except:
        print('can not get time from ntp server')


def auto_connect(id='undefined'):
    network.hostname(id)
    wlan = get_connection()
    if wlan is None:
        print("Could not initialize the network connection.")
    sync_time()
    print(time.localtime())
    led(1)

