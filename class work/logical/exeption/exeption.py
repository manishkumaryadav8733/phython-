class fundexception(Exception):
    pass

def check_fund(a):
    if a>10000:
        print("complete fund")
    else:
        raise fundexception(f"insufficent fund - wait for more{10000-a} amount")

print("started")
try:
    check_fund(3000)
except fundexception as e:
    print(e)
print("endend")