from typing import List, Dict, Any


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = self.buildTrie(wordDict)
        return self.wordBreakRecTrie(s, 0 , trie)

    # Try a Trie to reduce time complexity (will add space complexity)
    def wordBreakRec(self, s: str, idx: int, wordDict: List[str]) -> List[str]:
        if idx > len(s) - 1:
            return [""]
        res = []
        for word in wordDict:
            if s.startswith(word, idx):
                for sent in self.wordBreakRec(s, idx + len(word), wordDict):
                    res.append(word + " " + sent if sent else word)
        return res

    def wordBreakRecTrie(self, s: str, idx: int, trie: Dict[str, Any]) -> List[str]:
        if idx > len(s) - 1:
            return [""]
        res = []
        tnode = trie
        while idx < len(s) and s[idx] in tnode:
            tnode = tnode[s[idx]]
            if "#" in tnode:
                for sent in self.wordBreakRecTrie(s, idx + 1, trie):
                    res.append(tnode["#"] + " " + sent if sent else tnode["#"])
            idx += 1
        return res

    def buildTrie(self, wordDict: List[str]) -> Dict[str, Any]:
        trie = {}
        for word in wordDict:
            tnode = trie
            for ch in word:
                if ch not in tnode:
                    tnode[ch] = {}
                tnode = tnode[ch]
            tnode["#"] = word
        return trie


if __name__ == "__main__":
    print(Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
