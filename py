import telebot
from datetime import datetime

# Bot tokeningizni bu yerda kiriting
bot = telebot.TeleBot("YOUR_BOT_TOKEN_HERE")

# Haftalik jadval (dushanbadan jumagacha, misol uchun dars vaqtlari)
timetable = {
    "Dushanba": "08:00 - Matematika\n10:00 - Fizika\n12:00 - Kimyo",
    "Seshanba": "08:00 - Tarix\n10:00 - Geografiya\n12:00 - Biologiya",
    "Chorshanba": "08:00 - Adabiyot\n10:00 - Ingliz tili\n12:00 - Rus tili",
    "Payshanba": "08:00 - Matematika\n10:00 - Informatika\n12:00 - Sport",
    "Juma": "08:00 - Fizika\n10:00 - Kimyo\n12:00 - Uy vazifasi tekshiruvi"
}

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Salom! /jadval buyrug'i bilan dushanbadan jumagacha jadvalni ko'ring.")

@bot.message_handler(commands=['jadval'])
def send_timetable(message):
    today = datetime.now().strftime("%A")  # Bugungi kun
    uz_days = {"Monday": "Dushanba", "Tuesday": "Seshanba", "Wednesday": "Chorshanba", 
               "Thursday": "Payshanba", "Friday": "Juma"}
    if today in uz_days:
        day = uz_days[today]
        jadval = timetable.get(day, "Bugun dam olish kuni.")
        bot.send_message(message.chat.id, f"Bugungi jadval ({day}):\n{jadval}")
    else:
        # To'liq haftalik jadval
        full_msg = "Haftalik jadval (Dushanbadan jumagacha):\n\n"
        for day, schedule in timetable.items():
            full_msg += f"{day}:\n{schedule}\n\n"
        bot.send_message(message.chat.id, full_msg)

bot.polling()
