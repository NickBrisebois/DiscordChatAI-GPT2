#!/usr/bin/python3

import argparse
from Bot.bot import ChatBot


def main():
    parser = argparse.ArgumentParser(description="Big Lez Chat Bot")
    parser.add_argument("--token", dest="token", help="Input")

    args = parser.parse_args()
    token = args.token
    client = ChatBot()
    client.run(token)



if __name__ == "__main__":
    main()