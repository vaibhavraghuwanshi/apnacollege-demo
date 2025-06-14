def reverse_first_last_letter(s):
    li=s.split(" ")
    new_str=""
    x=[]
    delimiter=" "
    for word in li:
        if len(word)>1:
            first=word[0]
            last=word[len(word)-1]
            middle=word[1:len(word)-1]
            new_str=last+middle+first
        x.append(new_str)
    return delimiter.join(x)

print(reverse_first_last_letter("my name is khan and i am not a terrorist"))