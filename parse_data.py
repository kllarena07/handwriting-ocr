import stow
from tqdm import tqdm

dataset_path = stow.join('Datasets', 'IAM_Words')

def parse_data():
    dataset, vocab, max_len = [], set(), 0

    words = open(stow.join(dataset_path, "words.txt"), "r").readlines()
    for line in tqdm(words):
        if line.startswith('#'):
            continue

        line_split = line.split(" ")
        if line_split[1] == "err":
            continue

        folder1 = line_split[0][:3]
        folder2 = line_split[0][:8]
        file_name = line_split[0] + ".png"
        label = line_split[-1].rstrip('\n')

        rel_path = stow.join(dataset_path, "words", folder1, folder2, file_name)
        if not stow.exists(rel_path):
            continue

        dataset.append([rel_path, label])
        vocab.update(list(label))
        max_len = max(max_len, len(label))

        return (dataset, vocab, max_len)