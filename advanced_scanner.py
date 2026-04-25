import scapy.all as scapy
import requests
import time

def get_vendor(mac_address):
    """អនុគមន៍សម្រាប់ទាញយកឈ្មោះក្រុមហ៊ុនផលិតទូរស័ព្ទ/កុំព្យូទ័រ តាមរយៈ MAC Address"""
    try:
        # យើងប្រើប្រាស់ API ឥតគិតថ្លៃដើម្បីឆែកមើល MAC
        url = "https://api.macvendors.com/" + mac_address
        response = requests.get(url, timeout=2)
        if response.status_code == 200:
            return response.text
        return "Unknown Device"
    except:
        return "Unknown Device"

def scan_network(ip_range):
    print("==========================================")
    print(" 🕵️‍♂️ Advanced ARP Network Scanner v2.0 ")
    print("==========================================")
    print(f"\n[+] Broadcasting ARP Requests to {ip_range} ...\n")
    
    # ១. បង្កើតកញ្ចប់ទិន្នន័យសួររក IP (ARP Request)
    arp_request = scapy.ARP(pdst=ip_range)
    
    # ២. បង្កើតកញ្ចប់ទិន្នន័យស្រែកប្រាប់គ្រប់គ្នា (Broadcast)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    # ៣. បញ្ចូលកញ្ចប់ទិន្នន័យទាំងពីរចូលគ្នា
    arp_request_broadcast = broadcast/arp_request
    
    # ៤. បញ្ជូនចេញ និងរង់ចាំចម្លើយត្រឡប់មកវិញ (srp = send and receive packets)
    answered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]
    
    print("IP Address\t\tMAC Address\t\t\tVendor (Device)")
    print("-------------------------------------------------------------------------")
    
    # ៥. បំបែកចម្លើយដែលទទួលបាន និងបង្ហាញលើអេក្រង់
    for element in answered_list:
        ip = element[1].psrc
        mac = element[1].hwsrc
        
        print(f"[*] Checking vendor for {mac} ...", end="\r") # លោតអក្សររង់ចាំ
        vendor = get_vendor(mac)
        time.sleep(1) # ផ្អាក ១វិនាទី កុំឱ្យគេ Block API យើង
        
        # បង្ហាញលទ្ធផលចុងក្រោយ
        print(f"{ip}\t\t{mac}\t\t{vendor}                  ")

# របៀបប្រើប្រាស់
if __name__ == "__main__":
    target = input("Enter Target IP Range (e.g., 192.168.1.1/24): ")
    scan_network(target)
    print("\n[!] Scan Finished.")