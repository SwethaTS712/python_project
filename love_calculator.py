def calculate_love_score(name1, name2):
    n3 = name1 + name2
    names = n3.lower()
    
    t = names.count("t")
    r = names.count("r")
    u = names.count("u")
    e = names.count("e")
    first = t + r + u + e
    
    l = names.count("l")
    o = names.count("o")
    v = names.count("v")
    e = names.count("e")
    second = l + o + v + e
    
    
    score = int(str(first) + str(second))
    print(score)
    
calculate_love_score("jerry", "tom")