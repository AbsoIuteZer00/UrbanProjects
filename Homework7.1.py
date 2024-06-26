file_name = 'poems_1.txt'
file = open(file_name, mode='w', encoding='utf8')
file_content = (f"# -*- coding: utf-8 -*- \nMy soul is dark - Oh! quickly string \nThe harp I yet can brook to hear; \n"
                "And let thy gentle fingers fling \nIts melting murmurs o'er mine ear. \n"
                "If in this heart a hope be dear, \nThat sound shall charm it forth again: \n"
                "If in these eyes there lurk a tear, \n'Twill flow, and cease to burn my brain. \n\n"
                "But bid the strain be wild and deep, \nNor let thy notes of joy be first: \n"
                "I tell thee, minstrel, I must weep, \nOr else this heavy heart will burst; \n"
                "For it hath been by sorrow nursed, \nAnd ached in sleepless silence, long; \n"
                "And now 'tis doomed to know the worst, \nAnd break at once - or yield to song.")
file.write(file_content)
file.close()
with open(file_name, mode='r', encoding='utf8') as file:
    for line in file:
        print(line, end='')

# Опертаор with контролирует вход в блок кода и выход из него. При выходе из блока кода закрывает его самостоятельно.
