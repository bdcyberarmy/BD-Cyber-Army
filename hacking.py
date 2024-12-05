import socket
import pyfiglet
from termcolor import colored

print(colored("************************************************", "red"))
print(colored("******************👾Hacker👾********************", "red"))
print(colored("***************** URL TO IP ********************", "red"))
print("Loading.../")

# Create a banner
banner = colored(pyfiglet.figlet_format("Domain To IP"), "green")
print(banner)

# Prompt user to enter the target domain
print(colored("************************************************", "red"))
domain_name = input(colored("Enter Your Target Domain: ", "blue"))
print(colored("************************************************", "red"))

# Try to get the IP address of the domain
try:
    ip = socket.gethostbyname(domain_name)
    print(colored(f"The IP address of {domain_name} is {ip}", "green"))
except socket.gaierror:
    print(colored(f"Unable to get IP address for the domain: {domain_name}", "red"))



















