#!/usr/bin/env python3

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
    parser.add_argument("--response_chance", 
                        dest="response_chance", 
                        help="How likely should the bot respond. For example: give 0.25 for a 25% chance, give 0 for no random responses.")
    parser.add_argument("-t", dest="test", action="store_true", help="Test responses in CLI.")

    args = parser.parse_args()

    if args.test:
        ai = ChatAI()
        ai.load_model()

        while True:
            inp = input("> ")
            print(ai.get_bot_response(author="h!", message=inp))

        return

    if args.genmodel:
        ai = ChatAI()
        ai.generate_models("355M", "./input.txt")
    else:
        client = ChatBot(args.response_chance)
        token = args.token
        client.run(token)


if __name__ == "__main__":
    main()
