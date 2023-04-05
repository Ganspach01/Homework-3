#Grace Anspach
#Abraham Lincoln Farewell Address
def locate_word(x,y):
    matches=[]
    index=0
    while index<len(x):
        if x[index:index+len(y)]==y:
            matches.append(index)
            index+=len(y)
    return matches

z= "My friends---No one, not in my situation, can appreciate my feeling of sadness at this parting. To this place, and the kindness of these people, I owe every thing. Here I have lived a quarter of a century, and have passed from a young to an old man. Here my children have been born, and one is buried. I now leave, not knowing when, or whether ever, I may return, with a task before me greater than that which rested upon Washington. Without the assistance of that Divine Being, who ever attended him, I cannot succeed. With that assistance I cannot fail. Trusting in Him, who can go with me, and remain with you and be every where for good, let us confidently hope that all will yet be well. To His care commending you, as I hope in your prayers you will commend me, I bid you an affectionate farewell."
print(locate_word(z,"people"))
print(locate_word(z,"assisstance"))
print(locate_word(z,"one"))
print(locate_word(z,"succeed"))
