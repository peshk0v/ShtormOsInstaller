import os
from time import sleep

print("HELLO FROM SHTORMOS!")
print("DISK PATRION")
os.system("lsblk")
disk = input("\nType name of disk > ")
devdisk = "/dev/" + disk
print("Please partion your disk")
input("\nTo start patrion click ENTER")
try: os.system(f"cfdisk {devdisk}")
finally:
    print("\nDisk partion succices!")
    os.system("lsblk")
    print("Formating partions")
    sleep(1)
    try: os.system(f"mkfs.fat -F32 {devdisk}p1")
    finally: 
        os.system(f"mkfs.ext4 {devdisk}p2")
        try: os.system(f"mkfs.fat -F32 {devdisk}p3")
        finally: 
            print("Disk formating succices!")