import gpt_2_simple as gpt2
import os
import random

class ChatAI:
    """ ChatAI class handles GPT2 responses and learning """
    def __init__(self) -> None:
        self.sess = gpt2.start_tf_sess()


    def load_model(self) -> None:
        """ Load a pregenerated model to use to generate responses """
        gpt2.load_gpt2(self.sess)


    def generate_models(self, name: str, data_path: str) -> None:
        """ Generate new models given a model name and data source path. Data source path being a pre-existing gpt2 learning model """
        model_name = name
        if not os.path.isdir(os.path.join("models", model_name)):
            print(f"Downloading {model_name} model...")
            gpt2.download_gpt2(model_name=model_name)

        gpt2.finetune(
            self.sess,
            data_path,
            model_name=model_name,
            batch_size=1,
            sample_every=100,
            sample_length=100,
            )
        gpt2.generate(self.sess)


    def get_bot_response(self, author: str, message: str) -> str:
        """ Get a response to a given message using GPT2 model """
        return gpt2.generate(self.sess,
                            model_name="124M",
                            length=random.randint(10, 30),
                            prefix=author + ": " + message,
                            temperature=0.9,
                            include_prefix=False,
                            return_as_list=True,
                            )[0]
