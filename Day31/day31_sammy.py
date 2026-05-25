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