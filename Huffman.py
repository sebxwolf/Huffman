# Text examples

T1 = 'O all you host of heaven! O earth! What else? And shall I couple hell? Oh, fie! Hold, hold, my heart, And you, ' \
     'my sinews, grow not instant old, But bear me stiffly up. Remember thee! Ay, thou poor ghost, whiles memory ' \
     'holds a seat In this distracted globe. Remember thee! Yea, from the table of my memory I’ll wipe away all ' \
     'trivial fond records, All saws of books, all forms, all pressures past That youth and observation copied there,' \
     ' And thy commandment all alone shall live Within the book and volume of my brain, Unmixed with baser matter. ' \
     'Yes, by heaven! O most pernicious woman! O villain, villain, smiling, damned villain! My tables! Meet it is I ' \
     'set it down That one may smile, and smile, and be a villain. At least I’m sure it may be so in Denmark. So, ' \
     'uncle, there you are. Now to my word.'

T2 = 'Habe nun, ach! Philosophie, Juristerei und Medizin, Und leider auch Theologie Durchaus studiert, mit heissem ' \
     'Bemühn. Da steh ich nun, ich armer Tor! Und bin so klug als wie zuvor; Heisse Magister, heisse Doktor gar Und ' \
     'ziehe schon an die zehen Jahr Herauf, herab und quer und krumm Meine Schüler an der Nase herum Und sehe, dass ' \
     'wir nichts wissen k̈onnen! Das will mir schier das Herz verbrennen. Zwar bin ich gescheiter als all die Laffen, ' \
     'Doktoren, Magister, Schreiber und Pfaffen; Mich plagen keine Skrupel noch Zweifel, Fürchte mich weder vor ' \
     'Hölle noch Teufel Dafür ist mir auch alle Freud entrissen, Bilde mir nicht ein, was Rechts zu wissen, Bilde ' \
     'mir nicht ein, ich k̈onnte was lehren, Die Menschen zu bessern und zu bekehren. Auch hab ich weder Gut noch ' \
     'Geld, Noch Ehr und Herrlichkeit der Welt; Es m̈ochte kein Hund so l̈anger leben! Drum hab ich mich der Magie ' \
     'ergeben, Ob mir durch Geistes Kraft und Mund Nicht manch Geheimnis würde kund; Dass ich nicht mehr mit saurem ' \
     'Schweiss Zu sagen brauche, was ich nicht weiss; Dass ich erkenne, was die Welt Im Innersten zusammenhält, ' \
     'Schau alle Wirkenskraft und Samen, Und tu nicht mehr in Worten kramen.'

'''
The frequency_count function takes a text input string and creates a dictionary (frequency_table) of characters found in
the text as keys and their absolute frequency as values. This is implemented through a for-loop through the text input 
string that checks whether the iterative is already a key in the dictionary and if not, creates it, and if it is, 
augments its value. The dictionary is then transformed, by swapping keys and values, which transforms the dictionary 
into a list of tuples which are sorted by frequency. This list of ordered tuples is then returned as output.

The cost of this operation is O(n) because the loop runs through n operations, and the lookup in the dictionary is 
constant cost, given that the length of the alphabet is fixed.
'''


def frequency_count(text):
    frequency_table = {}
    for i in text.lower():
        if i not in frequency_table:
            frequency_table[str(i)] = 1
        else:
            frequency_table[str(i)] = frequency_table[str(i)] + 1
    frequency_table = sorted([(v, k) for k, v in frequency_table.items()])
    return frequency_table


'''
The build_tree function first calls the frequency_count function on the text input string it is given, and then builds a 
Huffman tree from it. The function iterates through the list from lowest to highest frequency, at each step creating a
new node with the two character tuples with lowest frequency. The node is created as a nested list with two entries, the
sum of the two children's frequencies, and a nested list with the two tuples. The node is then inserted back into the 
list that its entries were extracted from, with the position chosen by a for loop that compares the nodes value with 
each entry from the originator list until the node value is larger than the iterator's value. This loop runs as long 
as the top level list is longer than 1. When it reaches length 1, the tree is complete and returned as a nested list.

The cost of this operation is constant, because it depends only on the length of the dictionary given as input, which 
depends only of the length of the alphabet and thus is fixed.
'''


def build_tree(text):
    tree = frequency_count(text)
    while len(tree) > 1:
        node = [tree[0][0] + tree[1][0], [tree.pop(0), tree.pop(0)]]
        for i in range(len(tree)):
            if node[0] > tree[i][0]:
                pass
            else:
                index = i
                break
        tree.insert(index, node)
    return tree


'''
The climb_tree function first calls the build_tree function on the text input it is given, gets a Huffman tree in the 
form of a nested list, and then assigns codes to each node of the tree. The function climbs the tree from its root, 
taking left and right steps. While climbing, the function builds a dictionary with characters from the tree-nodes 
making up the keys, and code assignments making up the values. The dictionary is updated at every step that encounters 
a leaf of the tree, which is detected with an if condition that checks whether the node contains a string. If a node 
does not contain a string, this means that another list is nested inside the node, and that we are on a branch rather 
than a leaf of the tree. In the case of a branch, the function continues climbing with right and left steps. Right 
steps at a 1 to the code string, left steps add a 0 to the code string.

The cost of this operation is constant, because it depends only on the length of the nested list it receives as an 
input. The length and depth of the nested list in turn depends only on the length of the alphabet, which, again,
is fixed.
'''


def climb_tree(text):
    tree = build_tree(text)[0][1]
    code = str()
    dictionary = {}

    def right_step(branch, code):
        branch = branch[0][1]
        code = code + str(1)
        if type(branch) == str:
            nonlocal dictionary
            dictionary[branch] = code
        else:
            right_step(branch, code)
            left_step(branch, code)

    def left_step(branch, code):
        branch = branch[1][1]
        code = code + str(0)
        if type(branch) == str:
            nonlocal dictionary
            dictionary[branch] = code
        else:
            right_step(branch, code)
            left_step(branch, code)

    right_step(tree, code)
    return dictionary


'''
The encode function calls the climb_tree function to get a dictionary of characters in the text with their code
assignments. It iterates through the input text string and creates an output text string where every character is
replaced with their code assignment. It then returns the encoded output string.

The cost of this operation is O(n), because each character needs to be replaced.
'''


def encode(text):
    dictionary = climb_tree(text)
    encoded_text = str()
    for character in text.lower():
        encoded_text += dictionary[character]
    return encoded_text


'''
The decode function requires the same dictionary used to encode a text string, and the encoded text as input. First, it
swaps the keys and values of the dictionary such that the codes are keys, and the characters are values. It then
iterates through the encoded text and checks whether it can find an iterate in the dictionary. If not, it adds the next
iterate and checks whether it can find this longer code in the dictionary. Once it finds a code sequence it can find in
the dictionary it adds the corresponding dictionary entry to the output string. Once the function has iterated through
the entire encoded text it has recovered the original text string and outputs it.

The cost of this  operation is O(n), because each character is recovered in turn. The length of the encoded string
is proportional to the alphabet used. More complex alphabets will require longer code strings. Regardless, this
increases the cost of the algorithm only by a constant.
'''


def decode(dictionary, code):
    dictionary = dict([(v, k) for k, v in dictionary.items()])
    text = str()
    index = 0
    for i in range(len(code)):
        if code[index:i+1] in dictionary:
            text = text + dictionary[code[index:i+1]]
            index = i + 1
    return(text)


print(climb_tree(T1))
print(huffman(T1))
print(climb_tree(T2))
print(huffman(T2))