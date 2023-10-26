import argparse

import requests


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="Lệnh để thực thi")
    args = parser.parse_args()

    if args.command == "hello_world":
        print("Hello, world!")
    elif args.command == "get_weather":
        response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Hà Nội&appid=YOUR_API_KEY")
        data = response.json()
        print(data["weather"][0]["main"])


if __name__ == "__main__":
    main()
