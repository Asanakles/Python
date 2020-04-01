import telebot
import config_stephan
import pyowm

bot = telebot.TeleBot(config_stephan.TOKEN)
owm = pyowm.OWM(config_stephan.owm_key)

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id, 'Hi! My name is Stephan, and i will help you, send me message "info" for get more information!')

@bot.message_handler(content_types=['text'])
def send_text(message):
	imput_text = message.text.lower()
	print (imput_text)
	if 'info' in imput_text:
		bot.send_message(message.chat.id, 'Hi, I can told you weather in every places! Just write key words "weather" and eny place" \nOther function in development....')

	#weather from openweathermap.org
	elif 'weather' in imput_text:		
		imput_text = imput_text.replace('weather','')

		try:
			observation = owm.weather_at_place(imput_text)
			w = observation.get_weather()
			bot.send_message(message.chat.id, 'Temperature in {0} is {1} degrees of celsius, speed of wind {2} m/s, sky - {3} '\
				.format( imput_text.title(), w.get_temperature('celsius')['temp'], w.get_wind()['speed'], w.get_detailed_status() ) )
		except:
			bot.send_message(message.chat.id, 'I don\'t know that city' )
		
		

	else:
		bot.send_message(message.chat.id, 'Upps... sorry bro, i don\'t know that now, maybe i can help you leater? =)\nSend me "info" if you forget my functionality...')


	#bot.send_message(message.chat.id, 'Hi')
	#if message.text.lower() == 'привет':
	#	bot.send_message(message.chat.id, 'Привет, мой создатель')
	#elif message.text.lower() == 'пока':
	#	bot.send_message(message.chat.id, 'Прощай, создатель')
	#bot.send_message(message.chat.id, imput_text)

#bot.send_message(message.chat.id, message.text)



bot.polling(none_stop=True)