class Trie:
    
    def search_level(self, current_level, current_prefix, words):
        #check for end symbol and add the prefix to the list
        if self.end_symbol in current_level:
            words.append(current_prefix)
        
        #process each letter in the current level in sorted order except for the end symbol
        #extend the prefix with the letter and recursively search the child level
        for letter in sorted(current_level.keys()):
            if letter != self.end_symbol:
                self.search_level(current_level[letter], current_prefix + letter, words)
        #return all words found
        return words

    def words_with_prefix(self, prefix):
        #create a list to store the words
        words = []
        #get the current level of the trie starting from the root
        current_level = self.root
        #iterate through the prefix
        for letter in prefix:
            #if the letter is not in the current level, return an empty list
            if letter not in current_level:
                return []
            #move to the next level
            current_level = current_level[letter]
            #use search_level to find all words with the prefix and retutn the list
        return self.search_level(current_level, prefix, words)

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current_level = self.root
        for letter in word:
            if letter not in current_level:
                current_level[letter] = {}
            current_level = current_level[letter]
        current_level[self.end_symbol] = True
