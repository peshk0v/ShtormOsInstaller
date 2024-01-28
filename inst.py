import os

print("HELLO FROM SHTORMOS!")
print("DISK PATRION")
os.system("lsblk")
disk = input("\nType name of disk > ")
devdisk = "/dev/" + disk
print("Please partion your disk")
input("\nTo start patrion click ENTER")
os.system(f"cfdisk {devdisk}")