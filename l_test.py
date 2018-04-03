
def applyRules(in_char):
    r = ""
    if in_char == 'b': #b -> ab
        r = 'ab'
    elif in_char == 'a': #a -> b
        r = 'b'
    else:
        r = in_char        
    return r

def processString(old_str):
    new_str = ""
    for ch in old_str:
        new_str = new_str + applyRules(ch)
    print(new_str)
    return new_str

def createSystem(num, axiom):
    start_str = axiom
    end_str = ""
    for i in range(num):
        end_str = processString(start_str)
        start_str = end_str
    return end_str


createSystem(10, "b")
