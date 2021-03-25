# https://www.askpython.com/python/examples/trie-data-structure

class TrieNode:

    def __init__(self, char=None):
        self.char = char
        self.is_end = False
        # this saves space complexity by only storing alphabet 
        # characters in the words instead of the whole aphabet
        self.children = {}  


# m is recursive TrieNode, n is children/keys
# Time Complexity:  all methods are O(n) 
# Space Complexity: O(m*n)
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True

    def contains(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return node.is_end

    def delete(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                break
        if node.is_end:
            node.is_end = False

    def longest_prefix(self, prefix):
        # return the longest prefix
        prefixes = self.word_search(prefix)
        if len(prefixes) == 0: return

        longest = prefixes[0]
        for prefix in prefixes:
            if len(prefix) > len(longest):
                longest = prefix
        return longest

    def word_search(self, prefix):
        # return all the words starting with prefix
        # example: search "he" -> (He, Here, Hear, Her, Hello)
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                node = None
                break

        if node is None: return []

        return self._dfs(node, prefix[:-1], [])

    def _dfs(self, node, prefix, result):
        
        if node.is_end:
            result.append(prefix + node.char)

        for child in node.children.values():
            self._dfs(child, prefix + node.char, result)

        return result

    def __str__(self):
        node = self.root

        def display(node, prefix, result):

            if node.is_end:
                result.append(prefix)

            for child in node.children.values():
                display(child, prefix + child.char, result)

            return result

        return str(display(node, '', []))



if __name__ == '__main__':
    trie = Trie()
    trie.insert("here")
    trie.insert("hear")
    trie.insert("he")
    trie.insert("hello")
    trie.insert("how")
    trie.insert("her")
    trie.insert("there")
    trie.insert("the")
    print(trie)

    print(trie.contains("here"))
    print(trie.contains("hear"))
    print(trie.contains("he"))
    print(trie.contains("hello"))
    print(trie.contains("how"))
    print(trie.contains("her"))

    # edge cases that fail
    print(trie.contains("herez"))
    print(trie.contains("zhear"))
    print(trie.contains("hee"))
    print(trie.contains("hell"))
    print(trie.contains("hhow"))
    print(trie.contains("herr"))

    print(trie.word_search('he'))

    print(trie.longest_prefix('h'))
    print(trie.longest_prefix('t'))

    print(trie)