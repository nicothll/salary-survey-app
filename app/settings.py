import pickle


def save_pkl(filename, data):
    with open(f"./settings/{filename}.pkl", "wb") as f:
        pickle.dump(data, f)


def read_pkl(filename):
    with open(f"./settings/{filename}.pkl", "rb") as f:
        return pickle.load(f)


MODEL = read_pkl("saved_steps")
GRID_MODEL = read_pkl("saved_steps")["grid_model"]

CATEGORIES = read_pkl("categories")

RATES = read_pkl("rates")
