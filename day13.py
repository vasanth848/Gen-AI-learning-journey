#arguments and types
def data(team_name,captain,tagline):
   print('my team',team_name,'team captain',captain,'tagline',tagline)
data('csk','msd','whistle podu')

def datas(team_name="CSK", captain="MSD", tagline="Whistle Podu"):
    print('my team', team_name, 'captain', captain, 'tagline', tagline)
datas()

def greetings(*students):
    for i in students:
        print('hi',i,'tommorow is holiday')
greetings('tes','gdg','tet')



