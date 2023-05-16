"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    dic={"f":"F","o":"0","o":"0","z":"Z","i":"1","m":"M","a":"@","n":"N"}
    result1 = [dic.get(c.lower(), c) for c in result]
    print(result1)
    return result1  