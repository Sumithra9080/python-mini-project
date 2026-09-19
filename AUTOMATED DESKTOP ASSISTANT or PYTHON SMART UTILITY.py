import datetime
import os
import platform
import subprocess
import sys
import webbrowser

def check_date_time():
    now = datetime.datetime.now()
    print("\nCurrent Date : ", now.strftime("%A, %d %B %Y"))
    print("Current Time : ", now.strftime("%I:%M:%S %p"))


def send_notification():
    title = input("Enter notification title: ").strip() or "Notification"
    message = input("Enter notification message: ").strip() or ""
    try:
        from plyer import notification
        notification.notify(
            title=title,
            message=message,
            app_name="Utility Toolbox",
            timeout=6,
        )
        print("Notification sent!")
    except ImportError:
        print("The 'plyer' package is required for notifications.")
        print("Install it with: pip install plyer")
    except Exception as e:
        print(f"Could not send notification: {e}")


def generate_qr_code():
    data = input("Enter the URL or text to encode: ").strip()
    if not data:
        print("Nothing entered, cancelling.")
        return
    try:
        import qrcode
        img = qrcode.make(data)
        filename = "qr_code.png"
        # Avoid overwriting an existing file
        counter = 1
        while os.path.exists(filename):
            filename = f"qr_code_{counter}.png"
            counter += 1
        img.save(filename)
        print(f"QR code saved as: {os.path.abspath(filename)}")

        open_it = input("Open the image now? (y/n): ").strip().lower()
        if open_it == "y":
            _open_file(filename)
    except ImportError:
        print("The 'qrcode' package is required.")
        print("Install it with: pip install qrcode[pil]")
    except Exception as e:
        print(f"Could not generate QR code: {e}")


def _open_file(path):
    """Open a file with the OS default application."""
    try:
        if platform.system() == "Windows":
            os.startfile(path)  # type: ignore[attr-defined]
        elif platform.system() == "Darwin":
            subprocess.run(["open", path])
        else:
            subprocess.run(["xdg-open", path])
    except Exception as e:
        print(f"Could not open file automatically: {e}")

              
def search_play_youtube():
    query = input("Enter the video name/search term: ").strip()
    if not query:
        print("Nothing entered, cancelling.")
        return
    try:
        import pywhatkit
        print(f"Searching and playing '{query}' on YouTube...")
        pywhatkit.playonyt(query)
    except ImportError:
        print("The 'pywhatkit' package is required.")
        print("Install it with: pip install pywhatkit")
        # Fallback: at least open a YouTube search in the browser
        fallback = input("Open a YouTube search in your browser instead? (y/n): ")
        if fallback.strip().lower() == "y":
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    except Exception as e:
        print(f"Could not play video: {e}")


def open_google():
    webbrowser.open("https://www.google.com")
    print("Opening Google...")



def open_website():
    url = input("Enter the website URL (e.g. example.com): ").strip()
    if not url:
        print("Nothing entered, cancelling.")
        return
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    webbrowser.open(url)
    print(f"Opening {url} ...")



def calculator():
    import ast
    import operator

    # Only allow a safe subset of operators (no eval() of arbitrary code)
    allowed_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.Mod: operator.mod,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
        ast.FloorDiv: operator.floordiv,
    }

    def safe_eval(node):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError("Invalid constant in expression")
        elif isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type not in allowed_operators:
                raise ValueError("Operator not allowed")
            return allowed_operators[op_type](
                safe_eval(node.left), safe_eval(node.right)
            )
        elif isinstance(node, ast.UnaryOp):
            op_type = type(node.op)
            if op_type not in allowed_operators:
                raise ValueError("Operator not allowed")
            return allowed_operators[op_type](safe_eval(node.operand))
        else:
            raise ValueError("Unsupported expression")

    expr = input("Enter a math expression (e.g. 12 * (3 + 4)): ").strip()
    try:
        parsed = ast.parse(expr, mode="eval").body
        result = safe_eval(parsed)
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception:
        print("Error: Invalid expression.")



_FALLBACK_JOKES = [
    "My mom said I should follow my dreams, so I went back to sleep.",

    "I decided to be productive today... but my bed had other plans.",

    "Life is short, so I smile whenever I get a chance — especially when food arrives.",

    "I don't need a motivational speaker. I need someone to tell me to stop using my phone.",

    "I planned to save money this month, but then online shopping happened.",

    "My biggest achievement today was getting out of bed on the first alarm.",

    "I love weekends. They are like a free trial of happiness.",

    "I told myself, 'Just five more minutes on the phone.' Two hours later, here we are.",

    "Being an adult is mostly saying, 'I'll do it tomorrow.'",

    "I am not lazy. I am just on energy-saving mode."

    "My mom said I should follow my dreams, so I went back to sleep.",

    "I decided to be productive today... but my bed had other plans.",

    "Life is short, so I smile whenever I get a chance — especially when food arrives.",

    "I don't need a motivational speaker. I need someone to tell me to stop using my phone.",

    "I planned to save money this month, but then online shopping happened.",

    "My biggest achievement today was getting out of bed on the first alarm.",

    "I love weekends. They are like a free trial of happiness.",

    "I told myself, 'Just five more minutes on the phone.' Two hours later, here we are.",

    "Being an adult is mostly saying, 'I'll do it tomorrow.'",

    "I am not lazy. I am just on energy-saving mode.",

    "I tried to organize my life, but I couldn't find the right folder.",

    "My brain has too many tabs open, and I don't know where the music is coming from.",

    "I started exercising today. I walked to the fridge and came back.",

    "I don't have a six-pack, but I have a snack pack.",

    "I was going to clean my room, but then I remembered I am a student.",

    "My alarm clock and I have a toxic relationship. It keeps waking me up.",

    "I need a six-month vacation, twice a year.",

    "I am great at multitasking. I can waste time in several ways at once.",

    "My wallet is like an onion. Opening it makes me cry.",

    "I wanted to become an early bird, but I prefer sleeping like a normal human.",

    "My phone battery lasts longer than my motivation.",

    "I don't procrastinate. I simply wait until the last minute to create pressure.",

    "Today I did absolutely nothing, and honestly, I deserve a certificate.",

    "I have a lot of hobbies. Mostly starting things and never finishing them.",

    "I asked my computer for a break. It said, 'Sure, I'll crash.'",

    "Why do programmers prefer dark mode? Because light attracts bugs.",

    "Why did the programmer go broke? Because he used all his cache.",

    "Why was the computer cold? Because it left its Windows open.",

    "Why do programmers love coffee? Because it helps them Java.",

    "Why don't programmers like nature? Because it has too many bugs.",

    "I told my computer I needed a break, and now it won't stop showing me ads for vacations.",

    "My code works perfectly... I have no idea why.",

    "There are two hard things in programming: naming things and forgetting what you named them.",

    "I don't always test my code, but when I do, I do it in production.",

    "A programmer's favorite place? The cache.",

    "Why did the function feel lonely? Nobody called it.",

    "Why did the loop break up with the programmer? It needed some space.",

    "I love debugging. It feels like being a detective in a crime movie where I am also the criminal.",

    "My code has no bugs. It just has unexpected features.",

    "I would tell you a UDP joke, but you might not get it.",

    "Why did the Python programmer bring a snake to class? Because it was his favorite language.",

    "Programming is easy. You only need to know how to Google the error message.",

    "My computer is smarter than me. At least it knows when to restart.",

    "I wrote a program that cleans my room. It keeps returning 'File not found.'",

    "My sleep schedule is like my code — completely unpredictable.",

    "I studied for five hours and remembered everything for about five minutes.",

    "College taught me many things, especially how to survive on very little sleep.",

    "My assignment deadline is my strongest source of motivation.",

    "I don't need coffee to survive college. I need coffee to understand the lecture.",

    "Student life: attend class, take notes, forget everything, repeat.",

    "My laptop and I have one thing in common — we both need charging after a long day.",

    "I opened my textbook to study, and somehow my phone opened by itself."
]
    

def tell_joke():
    try:
        import pyjokes
        print("\n" + pyjokes.get_joke())
    except ImportError:
        import random
        print("\n" + random.choice(_FALLBACK_JOKES))
        print("(Tip: pip install pyjokes for a much bigger joke library.)")



def system_info():
    print("\n--- System Information ---")
    print(f"OS            : {platform.system()} {platform.release()}")
    print(f"OS Version    : {platform.version()}")
    print(f"Machine       : {platform.machine()}")
    print(f"Processor     : {platform.processor() or 'Unknown'}")
    print(f"Python Version: {platform.python_version()}")

    try:
        import psutil
        cpu_percent = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage("/")
        print(f"CPU Usage     : {cpu_percent}%")
        print(f"RAM Usage     : {mem.percent}% "
              f"({mem.used // (1024**2)} MB / {mem.total // (1024**2)} MB)")
        print(f"Disk Usage    : {disk.percent}% "
              f"({disk.used // (1024**3)} GB / {disk.total // (1024**3)} GB)")
    except ImportError:
        print("(Install 'psutil' for CPU/RAM/Disk stats: pip install psutil)")
    except Exception as e:
        print(f"Could not read extended system stats: {e}")


MENU_ACTIONS = {
    "1": check_date_time,
    "2": send_notification,
    "3": generate_qr_code,
    "4": search_play_youtube,
    "5": open_google,
    "6": open_website,
    "7": calculator,
    "8": tell_joke,
    "9": system_info,
}


def print_menu():
    print("\n" + "=" * 45)
    print("           UTILITY TOOLBOX MENU")
    print("=" * 45)
    print("1. Check Current Date & Time")
    print("2. Send Custom Desktop Notification")
    print("3. Generate QR Code from URL / Text")
    print("4. Search & Play YouTube Video")
    print("5. Open Google")
    print("6. Open a Website")
    print("7. Calculator")
    print("8. Tell a Random Joke")
    print("9. System Information")
    print("10. Exit Program")
    print("=" * 45)


def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-10): ").strip()

        if choice == "10":
            print("Goodbye! 👋")
            sys.exit(0)

        action = MENU_ACTIONS.get(choice)
        if action:
            try:
                action()
            except KeyboardInterrupt:
                print("\nCancelled.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")


if __name__ == "__main__":
    main()
