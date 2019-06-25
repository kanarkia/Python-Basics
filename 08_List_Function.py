lucky_numbers = [4,8,9,18,42,56]
friends = ['Kevin', 'Jack', 'Jane', 'Oscar', 'Toby']
print(friends)
print(lucky_numbers)

#friends.extend(lucky_numbers)
#print(friends)

'''''''''
friends.append('Olek')
print(friends)

friends.insert(1, 'Aleksander')
print(friends)

friends.remove('Toby')
print(friends)

friends.clear()
print(friends)
'''''''''

friends.pop()
print(friends)

print(friends.index('Jane'))

print(friends.count('Jane'))

friends.sort()
lucky_numbers.sort()

print(friends)
friends2 = friends.copy()
print(friends2)

