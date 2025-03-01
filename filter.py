nums=["apple","banana","orange","kiwi"]

print(list(filter(lambda name: name if len(name)>5 else None,nums)))