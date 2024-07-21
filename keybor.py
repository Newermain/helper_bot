from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# --- Меню типа 'Бар' ---

btnMain = KeyboardButton('⬅️Главное меню')
btnNaz0 = KeyboardButton('⬅️Назад в функционал')

# ---- Main menu ----
btnFAQ = KeyboardButton('⚠️Информация о боте')
btnSLC = KeyboardButton('📝Возможности')
btnPod = KeyboardButton('💰Подписка')
mainMenu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnFAQ, btnSLC, btnPod)

# ---- Money Menu ----
btnHELP = KeyboardButton('📕Помощь')
btnBUY = KeyboardButton('💰Оплатить')
Monmenu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnHELP, btnBUY ,btnMain,)

# ---- Func Menu ----
btnSys = KeyboardButton('Управление системой')
btnInf = KeyboardButton('Инфа о системе')
btnZad = KeyboardButton('Управление процессами')
btnMic = KeyboardButton('Звук')
Funcmenu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnSys, btnInf, btnZad, btnMain, btnMic)

# ---- PC Menu ----
btnScr = KeyboardButton('📸Сделать скриншот экрана')
btnOff = KeyboardButton('⚡Завершение работы ПК')
pcmenu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnScr, btnOff, btnNaz0)

# ---- Sound Menu ---- 
btnVikl = KeyboardButton('🔴Выкл звук')
btnVkl = KeyboardButton('🟢Вкл звук')
btnUb = KeyboardButton('🔈Изменить громкость')
Soumenu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnVikl, btnVkl, btnNaz0, btnUb)

# ---- Process Menu ----
btnProc = KeyboardButton('⭐Запущенные процессы')
btnOfP = KeyboardButton('⛔Завершение процесса')
Processmenu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnProc, btnOfP, btnNaz0)

# ---- Process2menu ----
btnProc2 = KeyboardButton('Firefox')
btnOfP2 = KeyboardButton('Discord')
btnOf3 = KeyboardButton('Steam')
btnOf5 = KeyboardButton('Telegram')
Process2menu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnProc2, btnOfP2, btnOf3, btnOf5, btnNaz0)

# ---- Info Menu ----
btnTemp = KeyboardButton("Температура")
btnKom = KeyboardButton('Комплектующие')
Infomenu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnTemp, btnKom, btnNaz0)