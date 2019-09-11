class TrieNode:

    def __init__(self):
        self.children = [None]*26
        self.is_end_of_word = None

class Trie:
    
    def __init__(self):
        self.root = self.get_node()
    
    def get_node(self):
        return TrieNode()

    def _char_to_index(self, ch):
        return ord(ch) - ord('a')
    
    def insert(self, word):
        
        temp = self.root
        length = len(word)

        for level in range(length):
            index = self._char_to_index(word[level])
            
            if not temp.children[index]:
                temp.children[index] = self.get_node()
            temp = temp.children[index]

        temp.is_end_of_word = True

    def search(self, word):
        temp = self.root
        length = len(word)

        for level in range(length):
            index = self._char_to_index(word[level])

            if not temp.children[index]:
                return False
            temp = temp.children[index]
        
        return (not temp is None) and (temp.is_end_of_word)

def main(): 
    # Input keys (use only 'a' through 'z' and lower case) 
    keys = ["the","a","there","anaswe","any", 
            "by","their"] 
    output = ["Not present in trie", 
              "Present in trie"] 
  
    # Trie object 
    t = Trie() 
  
    # Construct trie 
    for key in keys: 
        t.insert(key) 
  
    # Search for different keys 
    print("{} ---- {}".format("the",output[t.search("the")])) 
    print("{} ---- {}".format("these",output[t.search("these")])) 
    print("{} ---- {}".format("their",output[t.search("their")])) 
    print("{} ---- {}".format("thaw",output[t.search("thaw")])) 
  
if __name__ == '__main__': 
    main() 