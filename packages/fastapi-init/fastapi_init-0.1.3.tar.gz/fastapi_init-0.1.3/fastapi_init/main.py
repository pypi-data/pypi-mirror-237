import argparse

import requests
import git


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="Set command process")
    parser.add_argument("project_name", default="fastapi_init", help="Lệnh để thực thi")
    parser.add_argument("version", default="main", help="Lệnh để thực thi")
    args = parser.parse_args()

    if args.command == "init_project":
        git.repo.Repo.clone_from(
            "git@git.rabiloo.net:tech/base/fastapi-init.git", f"./{args.project_name}",
            branch=args.version
        )
    elif args.command == "get_weather":
        response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Hà Nội&appid=YOUR_API_KEY")
        data = response.json()
        print(data["weather"][0]["main"])


if __name__ == "__main__":
    main()
