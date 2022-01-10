import random

import faker

from faker import Faker

import time

import colorama

from colorama import Fore


print(Fore.BLUE+""" __  .__   __.  _______   ______        _______  _______ .__   __.  _______ .______          ___   .___________.  ______   .______         
|  | |  \ |  | |   ____| /  __  \      /  _____||   ____||  \ |  | |   ____||   _  \        /   \  |           | /  __  \  |   _  \        
|  | |   \|  | |  |__   |  |  |  |    |  |  __  |  |__   |   \|  | |  |__   |  |_)  |      /  ^  \ `---|  |----`|  |  |  | |  |_)  |       
|  | |  . `  | |   __|  |  |  |  |    |  | |_ | |   __|  |  . `  | |   __|  |      /      /  /_\  \    |  |     |  |  |  | |      /        
|  | |  |\   | |  |     |  `--'  |    |  |__| | |  |____ |  |\   | |  |____ |  |\  \----./  _____  \   |  |     |  `--'  | |  |\  \----.   
|__| |__| \__| |__|      \______/      \______| |_______||__| \__| |_______|| _| `._____/__/     \__\  |__|      \______/  | _| `._____|   
                                                                                                                                           
.__   __.   ______   .___________. _______        _______    ___       __  ___  _______                                                    
|  \ |  |  /  __  \  |           ||   ____| _    |   ____|  /   \     |  |/  / |   ____|                                                   
|   \|  | |  |  |  | `---|  |----`|  |__   (_)   |  |__    /  ^  \    |  '  /  |  |__                                                      
|  . `  | |  |  |  |     |  |     |   __|        |   __|  /  /_\  \   |    <   |   __|                                                     
|  |\   | |  `--'  |     |  |     |  |____  _    |  |    /  _____  \  |  .  \  |  |____                                                    
|__| \__|  \______/      |__|     |_______|(_)   |__|   /__/     \__\ |__|\__\ |_______|                                                   
                                                                                            """)



print("NOTE: if you see the color red on any info it is critical information about the person you looked up")

faker.Faker()

fake = Faker()

name = ""

token = ["MzExNTQ1MjAzOTEzMDE1Mjkx.VAhn8J.fDJp_14mBGiIo2dCH8zx5hUVE3","NDQ0NjUzODE1Nzc0ODEzMjYw.LK3UHT.l7QdH3u0hL8K2GWw9oq6DsBVzv","OTEwMjM0OTI2MzczNDUyMTQc.AbDWaU.iy8CHLoRIVtv70zBZMFhfjgUDk","Mjc2MTgzNTI3MzkzNTI2ODk3.WFs5Ww.SVtvF1jC4-JZ3L_ODi5AagXEGuz","Nzc1OTc2NTM3Mzc4NDczNzE1.AxW7w-.vlE7uAdps5RK4HeYPqfgtViOWZn"]

tokensel = random.choice(token)

age = [10,12,11,16,15,13,14,20,17,18,19,21]

agesel = random.choice(age)

number = [2072190992,5825298029,2164928262,2175322058,4098870748]

numsel = random.choice(number)

def about(name):

    print(Fore.GREEN + "[+].")

    time.sleep(1)

    print("[+]..")

    time.sleep(1)

    print("[+]...")

    time.sleep(1)

    print("[+]....")

    time.sleep(1)

    print("[+].....")

    time.sleep(1)

    print("[+] User Found.")

    time.sleep(1)

    print("RealName: "+fake.name())

    time.sleep(1)

    print("[+] Age: "+ str(agesel))

    time.sleep(1)

    print("[+] Instagram: www.instagram.com/users/"+name)

    time.sleep(1)

    print("[+] Reddit: www.reddit.com/users/"+name)

    time.sleep(1)

    print("[+] Facebook: www.facebook.com/profile/"+name)

    time.sleep(1)

    print("[+] Twitter: www.twitter.com/"+name)

    time.sleep(1)

    print(Fore.RED+"[+] Phone Number: "+ str(numsel))

    time.sleep(1)

    print(Fore.RED+"[+] Address: "+fake.address())

    time.sleep(1)

    print(Fore.RED+"[+] Discord Token: "+tokensel)

    time.sleep(1)

    print(Fore.GREEN+"[+] Email:" +" "+ name + "@gmail.com")

    time.sleep(1)


about("NetworkChuck")

