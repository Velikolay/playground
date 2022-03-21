from typing import List, Dict


def build_trie(words: List[str]) -> Dict[str, Dict]:
    trie = dict()
    for word in words:
        curr = trie
        for ch in word:
            if ch not in curr:
                curr[ch] = dict()
            curr = curr[ch]
        curr["word"] = word
    return trie


if __name__ == "__main__":
    print(build_trie(["asd", "dasas", "das", "sada", "asdef"]))
