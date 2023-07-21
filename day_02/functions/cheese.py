def cheeseshop(kind, *arguments, **keywords):
    print("do you have", kind)
    print("i'm sorry we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny,sir.", "It's very , VERY runny sir.",
           shopkeeper="sandeepSandy", client="raju", sketch="cheese shop sketch")
