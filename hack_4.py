"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    print("/b")
    result = "fooziman"
    for n in result.split():
        result = n[0:-1] + n[-1].upper()        
    print("/b")
    return result