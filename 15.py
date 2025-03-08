Dict=dict([(1,'kittu'), (2,'praneetha'), (3,'pavani'), (4,'Rupi'), (5,'priya')])
print("Dictionary with each item as a pair:",Dict)

Dict[6]='Samatha'
print("\n Dictionary with new item added:", Dict)

Dict[3]='gnana'
print("\n Dictionary with updated values:", Dict)

del Dict[6]
print("\n Accessing on evalue in Dictionary:", Dict)

Dict1={1: 'kittu', 2:'praneetha', 3:{'Age':19, 'Branch':'DS', ' Year' : 'Third Year'}}
print("\n Nested loop Dictionary:", Dict1)

print("\n Accessing an element of a Nested Dictionary:", Dict[2])