# Huffman Tree

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


def frequency_count(text):
    frequency_table = {}
    for i in text.lower():
        if i not in frequency_table:
            frequency_table[str(i)] = 1
        else:
            frequency_table[str(i)] = frequency_table[str(i)] + 1
    frequency_table = sorted([(v, k) for k, v in frequency_table.items()])
    return frequency_table


def build_tree(text):
    forest = frequency_count(text)
    while len(forest) > 1:
        node = [forest[0][0] + forest[1][0], [forest.pop(0), forest.pop(0)]]
        for i in forest:
            if node[0] > i[0]:
                pass
            else:
                index = i[0]
                break
        forest.insert(index, node)
    return forest


def climb_tree(forest):
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

    right_step(forest, code)
    return dictionary


def huffman(text):
    dictionary = climb_tree(build_tree(text))
    encoded_text = str()
    for character in text.lower():
        encoded_text += dictionary[character]
    return encoded_text


print(climb_tree(build_tree(T1)))
print(huffman(T1))
print(climb_tree(build_tree(T2)))
print(huffman(T2))


