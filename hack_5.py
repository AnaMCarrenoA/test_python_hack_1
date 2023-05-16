"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    print("/b")
    result = "fooziman"
    result=result.replace("fooziman","f00z1m@n",1)
    print("/b")
    return result  