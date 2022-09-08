#psuedo-code styling program. Uses python as a base, so works best for that language.
#A program which takes psuedocode as text, and returns (semi) styled HTML/CSS. 

import sys
import re
from mutility import readLines

def parse(s):
    """Parses a string of pseudo code into some html with inline styling."""
    #comments
    #keywords
    #   return, if, def, else, elif, for, while, or, and, not, in
    #special characters
    #   :, =, (), [], >, <, <=, >=, %, &, ^, +, -, \-
    #vals
    #   numbers, bools, strings

    #skeleton:
    #   use regex matching to find all instances of special characters/phrases, colors them appropriately.

    #replacement definitions
    #SpecialCharacters (defaults yellow)
    specialRe   = r'(?::|=|\(|\)|>|<|%|&|\^|\+|-|/|\*|\[|\])'
    specialRepl = lambda x: r'<span style="color:rgb(200,146,40);">' + x.group(0) + r'</span>'
    #keywords (defaults blue)
    keywordRe   = r'\b(?:return|if|def|else|elif|for|while|or|and|not|in|try|except|type|break|continue|pass)\b' 
    keywordRepl = lambda x: r'<span style="color:rgb(50,50,240);">' + x.group(0) + r'</span>'
    #Values (defaults greenish)
    typeRe      = r'\b(?:true|false)\b'
    typeRepl    = lambda x: r'<span style="color:rgb(75,255,140);">' + x.group(0) + r'</span>'
    #comments (defaults green)
    commentRe   = r'(?:#[^\n]*|"""[^(?:""")]*""")'
    commentRepl = lambda x: r'<span style="color:rgb(60,130,60);">' + x.group(0) + r'</span>'

    s = re.sub(specialRe, specialRepl, s)
    s = re.sub(keywordRe, keywordRepl, s)
    s = re.sub(typeRe, typeRepl, s)
    s = re.sub(commentRe, commentRepl, s)

    #wrap with pre, code tags
    s = r'<pre style="display:block;width:auto;margin:10px;padding:20px;background-color:rgb(30,30,30);color:rgb(230,230,230);"><code>' + s + r'</pre></code>'


    return s

def _tests():
    #tests parse function
    simple = "============================================================="
    keywords = """return if def
    else
    elif while or and not in try
    except type"""
    special = """: = ( ) < > = - +  * * [ ] """
    types   = """123 120938 whawjoi 190283127 asdci 12037 false true " Text." tt ++ "Bigtesting
    " """
    comments = """#This is a comment
    Not a comment
    #Another comment
    """
    multilineComment = 'This comes\n\n before the ocmment""" This\nis\na\nmultiline\ncomment"""This\nIsthestuff \nAfter.'

    ex1="""
c = 0
for i in range(100):
    c += i
return c
"""

    ex2="""
    def f(a):
        return a + 2
    """
    
    print(parse(ex2))

if __name__ == "__main__":
    _tests()
    """
    path = sys.argv[1]
    f = open(path, 'r')
    parsed = parse(f.readlines())
    f.close()

    if len(sys.argv) > 2:
        #print to file
        outputPath = sys.argv[2]
        f = open(outputPath, 'w')
        f.write(parsed)
        f.close()
    else:
        print(parsed)
        """