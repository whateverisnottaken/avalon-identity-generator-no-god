import random

names = ['玩家1', '玩家2', '玩家3', '玩家4', '玩家5', '玩家6']
#modify names to change the players when gamers are changed.

file1 = open(names[0] + '.txt', 'w')
file2 = open(names[1] + '.txt', 'w')
file3 = open(names[2] + '.txt', 'w')
file4 = open(names[3] + '.txt', 'w')
file5 = open(names[4] + '.txt', 'w')
file6 = open(names[5] + '.txt', 'w')
files = [file1, file2, file3, file4, file5, file6]
gen = ['梅林','莫甘娜','平民','平民','刺客','派西维尔']
for i in range(100):
	random.shuffle(gen)
	for j in range(6):
		files[j].write(str(i) + '\n')
		files[j].write('您的身份是：' + str(gen[j]))
	morgana = names[gen.index('莫甘娜')]
	assassin = names[gen.index('刺客')]
	merlin = names[gen.index('梅林')]
	gods = [merlin, morgana]
	random.shuffle(gods)
	vallains = [morgana, assassin]
	random.shuffle(vallains)
	files[gen.index('梅林')].write('\n两个坏人是：' + vallains[0] + '、' + vallains[1])
	files[gen.index('派西维尔')].write('\n梅林和莫甘娜是：' + gods[0] + '、' + gods[1])
	files[gen.index('刺客')].write('\n盟友-莫甘娜是：' + morgana)
	files[gen.index('莫甘娜')].write('\n盟友-刺客是：' + assassin)
	for file in files:
		file.write('\n您本局的开车数字是：')
		for i in range(5):
			file.write(str(random.randrange(0, 200) + random.randrange(1, 50)) + ' ')
		file.write('\n---------------------------------------------------------------------------\n')
