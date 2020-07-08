import telebot

print('/start')

def trans(text):
	bbb = 0
	prt = ''
	ch1 = []
	ch = []
	ch = list(text)
	for i in range(len(ch)):
		if ch[i] == 'а':
			ch1.append('a')
		elif ch[i] == 'ь':
			bbb = 0
		elif ch[i] == 'Ь':
			bbb = 0
		elif ch[i] == 'ы':
			bbb = 0
		elif ch[i] == 'Ы':
			bbb = 0
		elif ch[i] == 'э':
			bbb = 0
		elif ch[i] == 'Э':
			bbb = 0
		elif ch[i] == 'ъ':
			bbb = 0
		elif ch[i] == 'Ъ':
			bbb = 0
		elif ch[i] == 'А':
			ch1.append('A')
		elif ch[i] == 'б':
			ch1.append('b')
		elif ch[i] == 'Б':
			ch1.append('B')
		elif ch[i] == 'в':
			ch1.append('v')
		elif ch[i] == 'В':
			ch1.append('V')
		elif ch[i] == 'г':
			ch1.append('h')
		elif ch[i] == 'Г':
			ch1.append('H')
		elif ch[i] == 'Ґ':
			ch1.append('G')
		elif ch[i] == 'ґ':
			ch1.append('g')
		elif ch[i] == 'д':
			ch1.append('d')
		elif ch[i] == 'Д':
			ch1.append('D')
		elif ch[i] == 'e':
			ch1.append('е')
		elif ch[i] == 'E':
			ch1.append('E')
		elif ch[i] == 'є':
			ch1.append('ye')
		elif ch[i] == 'Є':
			ch1.append('Ye')
		elif ch[i] == 'ж':
			ch1.append('zh')
		elif ch[i] == 'Ж':
			ch1.append('Zh')
		elif ch[i] == 'з':
			ch1.append('z')
		elif ch[i] == 'З':
			ch1.append('Z')
		elif ch[i] == 'и':
			ch1.append('y')
		elif ch[i] == 'И':
			ch1.append('Y')
		elif ch[i] == 'і':
			ch1.append('i')
		elif ch[i] == 'І':
			ch1.append('I')
		elif ch[i] == 'ї':
			ch1.append('i')
		elif ch[i] == 'Ї':
			ch1.append('Y')
		elif ch[i] == 'Й':
			ch1.append('Y')
		elif ch[i] == 'й':
			ch1.append('i')
		elif ch[i] == 'К':
			ch1.append('K')
		elif ch[i] == 'к':
			ch1.append('k')
		elif ch[i] == 'Л':
			ch1.append('L')
		elif ch[i] == 'л':
			ch1.append('l')
		elif ch[i] == 'М':
			ch1.append('M')
		elif ch[i] == 'м':
			ch1.append('m')		
		elif ch[i] == 'Н':
			ch1.append('N')
		elif ch[i] == 'н':
			ch1.append('n')
		elif ch[i] == 'О':
			ch1.append('O')
		elif ch[i] == 'о':
			ch1.append('o')
		elif ch[i] == 'П':
			ch1.append('P')
		elif ch[i] == 'п':
			ch1.append('p')
		elif ch[i] == 'Р':
			ch1.append('R')
		elif ch[i] == 'р':
			ch1.append('r')
		elif ch[i] == 'С':
			ch1.append('S')
		elif ch[i] == 'с':
			ch1.append('s')
		elif ch[i] == 'Т':
			ch1.append('T')
		elif ch[i] == 'т':
			ch1.append('t')
		elif ch[i] == 'У':
			ch1.append('U')
		elif ch[i] == 'у':
			ch1.append('u')
		elif ch[i] == 'Ф':
			ch1.append('F')
		elif ch[i] == 'ф':
			ch1.append('f')
		elif ch[i] == 'Х':
			ch1.append('Kh')
		elif ch[i] == 'х':
			ch1.append('kh')
		elif ch[i] == 'Ц':
			ch1.append('Ts')
		elif ch[i] == 'ц':
			ch1.append('ts')
		elif ch[i] == 'Ч':
			ch1.append('Ch')
		elif ch[i] == 'ч':
			ch1.append('ch')
		elif ch[i] == 'Ш':
			ch1.append('Sh')
		elif ch[i] == 'ш':
			ch1.append('sh')
		elif ch[i] == 'Щ':
			ch1.append('Shch')
		elif ch[i] == 'щ':
			ch1.append('Shch')
		elif ch[i] == 'Ю':
			ch1.append('Yu')
		elif ch[i] == 'ю':
			ch1.append('iu')
		elif ch[i] == 'Я':
			ch1.append('Ya')
		elif ch[i] == 'я':
			ch1.append('ia')
		else:
			ch1.append(ch[i])
	for i in range(len(ch1)):
		prt = prt + ch1[i]
	return(prt)

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start'])
def start(message):
	prt = ''
	prt = str(str(message.chat.id) + '$%$&$%$' + str(message.chat.id) + '$%$&$%$' + str(message.from_user.first_name) + '$%$&$%$' + str(message.from_user.last_name) + '$%$&$%$' + str(message.from_user.username) + '\n')
	try:
		file = open('data.txt', 'a')
		file.write(prt)
		file.close()
	except:
		file = open('data.txt', 'w')
		file.write(prt)
		file.close()
	bot.send_message(message.chat.id, text='Привіт, я бот для перекладу українського тексту на\nофіційну латиницю (трансліт)')
	bot.send_message(message.chat.id, text='Відправ мені повідомлення з текстом для перекладу')

@bot.message_handler(content_types=['photo'])
def photo(message):
	bot.send_message(message.chat.id, 'Я не можу перекладати фото\nБудь ласка надішліть текст')

@bot.message_handler(content_types=['text'])
def text(message):
	txt = ''
	txt = trans(message.text)
	bot.send_message(message.chat.id, txt)

bot.polling(none_stop=True)