from constants import BIN_FILE, AUTHOR_SIGN
import markovify
import pickle
import os


class Generator:
    def __init__(self) -> None:
        self.combined_model = None
        for (dirpath, _, filenames) in os.walk("texts"):
            for filename in filenames:
                with open(os.path.join(dirpath, filename)) as f:
                    model = markovify.Text(f, retain_original=False,  well_formed=False)
                    if self.combined_model:
                        self.combined_model = markovify.combine(models=[self.combined_model, model])
                    else:
                        self.combined_model = model
        self.combined_model.compile()

    def get_phrase(self) -> str:
        sentence_size = 280 - 5 - len(AUTHOR_SIGN)
        return "\"" + self.combined_model.make_short_sentence(sentence_size) + "\" - " + AUTHOR_SIGN

if __name__ == '__main__':   
    if os.path.isfile(BIN_FILE):
        with open(BIN_FILE, 'rb') as f:
            generator = pickle.load(f)
    else:
        generator = Generator()
    with open(BIN_FILE, 'wb') as f:
        pickle.dump(generator, f)
    print(generator.get_phrase())
