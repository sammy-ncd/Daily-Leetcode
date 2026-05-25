'''

Problem:
https://leetcode.com/problems/implement-trie-prefix-tree/


'''


"""

Approach:
- hashmap for children
- boolean if this node marks the end of a full word

keep a sort of recursive structure each node will be a Trie itself


"""


class Trie(object):

    def __init__(self):
        self.children = {} # {symbol: child -> trie node}
        self.isWordNode = False 
        
    def insert(self, word):
        
        cur_node = self

        for i in range(len(word)):
            c = word[i]
    
            if c in cur_node.children:
                cur_node = cur_node.children[c]
            else:
                cur_node.children[c] = Trie()
                cur_node = cur_node.children[c]

        cur_node.isWordNode = True

    def search(self, word):

        cur_node = self
        
        for i in range(len(word)):
            c = word[i]

            if c in cur_node.children:
                cur_node = cur_node.children[c]
            else:
                return False

        return cur_node.isWordNode

    def startsWith(self, prefix):
        
        cur_node = self
        
        for i in range(len(prefix)):
            c = prefix[i]

            if c in cur_node.children:
                cur_node = cur_node.children[c]
            else:
                return False
            
        return True
    

# Just some chat gpt code to visualize the trie

def print_trie(node, prefix="", label="ROOT", is_last=True):
    marker = " *" if node.isWordNode else ""
    print(prefix + label + marker)

    children = list(node.children.items())

    for i in range(len(children)):
        char, child = children[i]
        last_child = i == len(children) - 1

        branch = "└── " if last_child else "├── "
        next_prefix = prefix + ("    " if is_last else "│   ")

        print_trie(child, next_prefix, branch + char, last_child)


# test trie to visualize

trie = Trie()

words = ["cat", "car", "cart", "dog", "door", "dot"]

for word in words:
    trie.insert(word)

print_trie(trie)
    

"""

Time Complexity:

let n = length of the input string

insert:
at most we have to go through and create a new Trie Node for each char in
the word so overall ----> O(n)

search:
in the case that the word exists we will scan through all letters in it
so overall ----> O(n)

startsWith:
in the case that the prefix exists we will scan through all letters in it
so overall ----> O(n)


Space Complexity:
let w = total amount of words in the trie, in the case that they are all unique
(no similar prefixes) we will have n*w trie nodes, so overall ---> O(wn)


"""