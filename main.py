from parse_data import parse_data
from configs import ModelConfigs

dataset, vocab, max_len = parse_data()

configs = ModelConfigs()
configs.vocab = "".join(vocab)
configs.max_text_length = max_len
configs.save()