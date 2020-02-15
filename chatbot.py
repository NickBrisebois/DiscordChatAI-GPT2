#!/usr/bin/python3

import gpt_2_simple as gpt2
import os
import argparse

def generate_models():
    model_name = "124M"
    if not os.path.isdir(os.path.join("models", model_name)):
        print(f"Downloading {model_name} model...")
        gpt2.download_gpt2(model_name=model_name)

    data_path = "./full.txt"
    sess = gpt2.start_tf_sess()
    gpt2.finetune(
        sess,
        data_path,
        model_name=model_name,
        steps=1000
    )
    gpt2.generate(sess)

def main():
    parser = argparse.ArgumentParser(description="Big Lez Chat Bot")
    parser.add_argument("--input", dest="input", help="Input")

    args = parser.parse_args()

    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess)
    gpt2.generate(sess,
        model_name="124M",
        prefix=args.input,
        length=1000,
        temperature=1,
        top_p=1,
        nsamples=100,
        batch_size=1, 
    )




if __name__ == "__main__":
    main()