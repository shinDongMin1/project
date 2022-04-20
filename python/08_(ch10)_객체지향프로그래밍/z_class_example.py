names = ["Messi", "Ramos", "Kim"]
positions = ["MF", "DF", "CF"]; numbers = [10, 4, 7]
players = [[name, position, number]     # 이차원 리스트
           for name, position, number in zip(names, positions, numbers)]
print(players)  # [['Messi', 'MF', 10], ['Ramos', 'DF', 4], ['Kim', 'CF', 7]]
print(players[0])   # ['Messi', 'MF', 10]
class SoccerPlayer(object):
    def __init__(self, name, position, numbers):
        self.name = name
        self.position = position
        self.b_num = numbers  # back number
    def change_b_num(self, new_number):
        local_var = self.b_num      # 로컬 변수.
        self.b_num = new_number
        return f'Back number of {self.name} is changed from {local_var} to {self.b_num}.'
    def __str__(self):
        return "%s: I play in %s with back number %d." % (self.name, self.position, self.b_num)

p_obj = [SoccerPlayer(name, position, number)
         for name, position, number in zip(names, positions, numbers)]
print(p_obj[0])     # Messi: I play in MF with back number 10.
print(p_obj[1])     # Ramos: I play in DF with back number 4.

print(p_obj[0].b_num)   # 1) messi의 등번호를 출력한다. # 10
print(p_obj[0].change_b_num(13))  # 2) 현재 messi의 등번호를 13으로 바꾼다.
# Back number of Messi is changed from 10 to 13.
# 3) Ramos의 position을 WF로 바꾸고 그 결과를 출력한다.
p_obj[1].position = 'WF';   print(p_obj[1].position)    # WF

