team_1 = 'Мастера кода'
team_2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
print('В команде %s участников %s!' % (team_1, team1_num))
print('В команде %s участников %s!' % (team_2, team2_num))
print('Итого сегодня в командах участников %s и %s!' % (team1_num, team2_num))
score_1 = 40
score_2 = 42
time_1 = 17934.8
time_2 = 18015.2
if score_1 < score_2 or score_1 == score_2 and time_1 < time_2:
    challenge_result = f'Победа команды {team_2}'
elif score_1 > score_2 or score_1 > score_2 and time_1 > time_2:
    challenge_result = f'Победа команды {team_1}'
else:
    challenge_result = 'Ничья'
tasks_total = score_1 + score_2
time_avg = round((time_1 + time_2) / tasks_total, 2)
print('Команда {} решила задач: {}'.format(team_2, score_2))
print('Команда {} решала задачи за {} с!'.format(team_2, time_2))
print(f'Команды решили {score_1} и {score_2} задач.')
print(challenge_result)
print(f'Сегодня было решено {tasks_total} задачи, в среднем по {time_avg} секунд на задачу')
