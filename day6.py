#LIST
players=['neymar','carlos','ramos','messi']
print(players)
print(type(players))

#INDEXING LIST
print(players[2])
print(players[-4])

#CHANING LIST
players[1]='ronaldo'
print(players)
players[1:3]='messi','marcelo','kroos'
print(players)
players.insert(3,'puyol')
print(players)
players.append('ronaldino')
print(players)
players.remove('messi')
print(players)
players.pop()
print(players)
players.sort()
print(players)
