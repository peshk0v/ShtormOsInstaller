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
    print("\nFormating partions")
    sleep(1)
    try: os.system(f"mkfs.fat -F32 {devdisk}p1")
    finally: 
        os.system(f"mkfs.ext4 {devdisk}p2")
        try: os.system(f"mkfs.fat -F32 {devdisk}p3")
        finally: 
            print("Disk formating succices!")
            sleep(1)
            print("\nMounting home dir")
            try: os.system(f"mount {devdisk}p2 /mnt")
            finally:
                try: os.system("mkdir /mnt/home")
                finally:
                    try: os.system(f"mount {devdisk}p3 /mnt/home")
                    finally: 
                        os.system("lsblk")
                        print("Gread")
                        sleep(1)
                        print("\nInstalling base")
                        try: os.system("pacstrap -i /mnt base linux linux-firmware sudo nano")
                        finally:
                            try: os.system("genfstab -U -p /mnt >> /mnt/etc/fstab")
                            finally:
                                try: os.system("arch-chroot /mnt /bin/bash")
                                finally: 
                                    try: os.system("cp data/linux/locale.gen /etc/locale.gen")
                                    finally: print("popa")