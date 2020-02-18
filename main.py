#!/usr/bin/python3

import argparse
from Bot.bot import ChatBot
from Bot.ai import ChatAI


def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Big Lez Chat Bot")
    parser.add_argument("--token", dest="token", help="Input")
    parser.add_argument("--genmodel",
                        dest="genmodel",
                        action="store_true",
                        help="generate new model")

    args = parser.parse_args()

    if args.genmodel:
        ai = ChatAI()
        ai.generate_models("124M", "./removespaces.txt")
    else:
        client = ChatBot()
        token = args.token
        client.run(token)


if __name__ == "__main__":
    main()
