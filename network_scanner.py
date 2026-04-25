import subprocess

print("==================================")
print("   Simple Network Scanner v1.0    ")
print("==================================")

# ពន្យល់អ្នកប្រើប្រាស់ពីរបៀបវាយ IP
print("Example: 192.168.1 (Do not add the last dot)")
base_ip = input("Enter the Base IP of your network: ")

print(f"\n[+] Scanning network {base_ip}.x ... (Checking first 20 IPs)\n")

# បង្កើតរង្វិលជុំ (Loop) ស្កេនពីលេខ 1 ដល់ 20 (ដើម្បីកុំឱ្យយូរពេក)
for i in range(1, 255):
    ip = f"{base_ip}.{i}"
    
    # បង្កើត Command Ping សម្រាប់ Linux (-c 1 គឺផ្ញើតែ១ដង, -W 1 គឺរង់ចាំតែ១វិនាទី)
    command = ['ping', '-c', '1', '-W', '1', ip]
    
    # បញ្ជាឱ្យ Python រត់ Command នេះដោយស្ងាត់ៗ (មិនបាច់លោតអក្សររញ៉េរញ៉ៃ)
    result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # ឆែកលទ្ធផល៖ បើ returncode == 0 មានន័យថាមានគេឆ្លើយតប (ម៉ាស៊ីនកំពុងបើក)
    if result.returncode == 0:
        print(f"[!] ACTIVE: Device found at {ip} 🟢")
    else:
        # បើគ្មានគេឆ្លើយតប យើងឱ្យវាដើររំលង (pass)
        pass

print("\n[+] Scan Complete!")