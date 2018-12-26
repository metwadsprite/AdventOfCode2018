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

S   a   n   t   a
83  97  110 116 97

23 days in dec until Santa?

1279?
"""

file = open('text.txt', 'r')
text = file.readline().strip('\\').split('\\')
file.close()
text = [int(i) for i in text]
text = [chr(i - 127900) for i in text]

uni = [chr(i) for i in range(1000)]

# for k in range(100):
#     print(k, end=' ')
#
#     shifted = [chr(ord(i) + k) for i in uni]
#
#     dict = {}
#     for index, letter in enumerate(uni):
#         dict[letter] = shifted[index]
#
#     mod_text = []
#     for c in text:
#         mod_text.append(dict[c])
#
#     for c in mod_text:
#             print(c, end='')
#     print()

shifted = [chr(ord(i) + 23) for i in uni]

dict = {}
for index, letter in enumerate(uni):
    dict[letter] = shifted[index]

mod_text = []
for c in text:
    mod_text.append(dict[c])

for c in mod_text:
        print(c, end='')
print()
