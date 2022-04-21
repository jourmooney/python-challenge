import requests
import os

def main():
    print("Welcome to IsItDown.py!")
    print("Please write a URL or URLs you want to check. (separated by comma)")
    # userinput = "google.com,         youtube.com, http://reddittadsfttt.com"
    userinput = input()
    url_list = userinput.split(",")
    for url in url_list:
        if "." not in url:
            print(f"{url} is not a valid URL.")
        else:
            url = url.strip().replace(" ", "").lower()
            if not url.startswith("http"):
                url = "http://" + url
            try:
                r = requests.get(url)
                if r.status_code == 200:
                    print(f"{url} is up!")
                else:
                    print(f"{url} is down!")
            except Exception as e:
                print(f"{url} is down!")
    question()

def question():
    ask = input("Do you want to start over? y/n ")
    if ask == "y":
        clear_console()
        main()
    elif ask == "n":
        print("k.bye!")
    else:
        print("That's not a valid answer.")
        question()

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

main()
