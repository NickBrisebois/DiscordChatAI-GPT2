import gpt_2_simple as gpt2
import os
import random

class ChatAI:
    def __init__(self):
        self.sess = gpt2.start_tf_sess()
        self.history = []

    def load_model(self):
        gpt2.load_gpt2(self.sess)

    # Generate new models given a model name and data source path
    def generate_models(self, name, data):
        model_name = name
        if not os.path.isdir(os.path.join("models", model_name)):
            print(f"Downloading {model_name} model...")
            gpt2.download_gpt2(model_name=model_name)

        data_path = data
        gpt2.finetune(
            self.sess,
            data_path,
            model_name=model_name,
            batch_size=1,
        )
        gpt2.generate(self.sess)

    def add_to_history(self, author, message):
        self.history.append(author + ": " + message+"\n\n")

        if len(self.history) > 4:
            del self.history[0]

    def get_bot_response(self, author, prefix):

        history_str = ""
        if len(self.history) > 0:
            history_str = "".join(self.history)
            del self.history[0]

        output = gpt2.generate(self.sess,
                            model_name="355M",
                            length=random.randint(20, 80),
                            prefix=history_str+author + ": " + prefix+"\n",
                            temperature=0.85,
                            include_prefix=False,
                            return_as_list=True,
                            )[0]

        self.history.append(author + ": " + prefix+"\n\n")

        output.encode("utf-8")
        lines = output.split("\n")

        style = ""
        foutput = []

        array_start = (len(self.history)*2)+1
        if len(self.history) == 1:
            array_start = 1

        # really ugly code but somehow works so i won't touch it again
        for line in lines[array_start::]:
            if line == "\n" or line == "": continue;

            if style == "" and len(line.split(": ")) > 1:
                style = line.split(": ")[0]
                foutput.append(line.split(": ")[1])
                self.history.append(line+"\n\n")
            elif style == line.split(": ")[0]:
                if len(line.split(": ")) > 1 and line.split(": ")[0] == style:
                    foutput.append(line.split(": ")[1])
                    self.history.append(line+"\n\n")
            elif style != line.split(": ")[0]:
                break

        return foutput

