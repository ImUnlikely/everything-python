def myfunc(text: str):
    assert type(text) == str # Ensure text is type str
    print(text)
    
myfunc(2)
myfunc("My text")