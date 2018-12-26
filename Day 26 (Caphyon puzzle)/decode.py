"""
- - -
Decode the following message, using this hint: letters to Santa

\127960\127978\127987\127977\127909\127974\127987\127909
\127978\127986\127974\127982\127985\127909\127993\127988
\127935\127909\127995\127982\127976\127993\127988\127991
\127923\127976\127982\127994\127991\127974\127941\127976
\127974\127989\127981\127998\127988\127987\127923\127976
\127988\127986\127909\127960\127994\127975\127983\127978
\127976\127993\127935\127909\127942\127988\127944\127909
\127927\127925\127926\127933\127909\127977\127988\127987
\127978

big mid word : 2 unique chars
2nd to last word : all 4 chars unique - 1279? 2018?
3rd to last word : 2 unique chars (bounds) with 'o' in the middle - Job? AoC?
"""


file = open('text.txt', 'r')
text = file.readline().strip().strip('\\').split('\\')
file.close()
text = [int(i) - 127900 for i in text]

text_set = list(set(text))
text_set.sort(key=lambda i : text.count(i), reverse=True)


def change(string, let1, let2):
    string = list(string)
    for i in range(len(string)):
        if string[i] == let1:
            for j in range(len(string)):
                if string[j] == let2:
                    string[j] = let1
                    break
            string[i] = let2
            break
    return ''.join(string)


common = ' etaoinshrdlcumwfgypbvkjxqz@.' # most frequent letters in english
# common = ' abcdefghijklmnopqrstuvwxyz@.' # alphabet in order

# copy paste this:
# common = change(common, '', '')

###############################################
# common = change(common, 'j', 's')
# common = change(common, 'd', 'e')
# common = change(common, 'd', 'n')
# common = change(common, 'k', 'd')
# common = change(common, 'a', 'c')
# common = change(common, 'l', 'm')
# common = change(common, ':', 'i')
# common = change(common, 'y', 'l')
################################################
# common = change(common, 'h', '.')
# common = change(common, 'b', 'c')
# common = change(common, 'b', 'o')
# common = change(common, 'h', 'y')
# common = change(common, 'w', 'h')
# common = change(common, 'z', 'p')
# common = change(common, 'j', '@')
# common = change(common, 'g', 'v')
################################################
# common = change(common, 'c', 'o')
# common = change(common, 'b', 'c')
# common = change(common, '@', 'c')
################################################
common = change(common, 'd', 's')
common = change(common, 'o', 'e')
common = change(common, 'i', 'n')
common = change(common, 'l', 'd')
common = change(common, 'c', 'm')
common = change(common, 'q', 'l')
common = change(common, 'q', 't')
common = change(common, 'q', 'c')
common = change(common, 'h', '.')
common = change(common, 'h', 'y')
common = change(common, 'z', 'p')
common = change(common, 'j', 'h')
common = change(common, 'z', '@')
common = change(common, 'q', 'u')
common = change(common, 'q', 'r')
common = change(common, 'z', 'v')
common = change(common, 'k', 'b')
common = change(common, 'x', 'j')
common = change(common, 'q', ':')
################################################
# common = change(common, 'k', '1')
# common = change(common, 'z', '2')
# common = change(common, 'g', '3')
# common = change(common, 'w', '4')
# common = change(common, 'f', '5')
# common = change(common, 'x', '6')
################################################
common = change(common, 'k', 'A')
common = change(common, 'z', 'C')
common = change(common, 'g', '2')
common = change(common, 'w', '0')
common = change(common, 'f', '1')
common = change(common, 'x', '8')


dict = {}

for i in range(len(text_set)):
    if i >= len(common):
        break
    dict[text_set[i]] = common[i]

for i in text:
    if i in dict:
        print(dict[i], end='')
    else:
        print('?', end='')
