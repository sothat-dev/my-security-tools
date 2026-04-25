import random
import string

print("==================================")
print("  Secure Password Generator v1.0  ")
print("==================================")

# សួរអ្នកប្រើប្រាស់ថាចង់បានលេខសម្ងាត់ប៉ុន្មានខ្ទង់ (ឧទាហរណ៍៖ 12, 16, 20)
try:
    length = int(input("How many characters do you want? (e.g., 16): "))
except ValueError:
    print("Please enter a valid number!")
    exit()

# ប្រមូលផ្ដុំតួអក្សរទាំងអស់ (អក្សរធំ អក្សរតូច លេខ និងសញ្ញា)
all_characters = string.ascii_letters + string.digits + string.punctuation

# ចាប់ឆ្នោតរើសតួអក្សរដោយចៃដន្យ (Random) តាមចំនួនដែលសុំ
password = "".join(random.sample(all_characters, length))

print("\n[+] Success! Here is your ultra-secure password:")
print("------------------------------------------------")
print(password)
print("------------------------------------------------")