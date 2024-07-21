from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import token  
import keybor as key
import logging
import os
from os import popen #библиотека для выполнения команд управления системой
from pyautogui import screenshot
import pyautogui
# from soundlib.sound import Sound
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
# from ctypes import *
import psutil



bot = Bot(token=token)
dp = Dispatcher(bot)

# --- Команды ---
@dp.message_handler(commands=['start','buy'])
async def main_start(message: types.Message):
    if "/start" in message.text.lower():
        await bot.send_message(message.from_user.id, 'Привет {0.first_name}, я бот для взаимодействия с вашим ПК.'.format(message.from_user), reply_markup= key.mainMenu) 
    elif "/buy" in message.text.lower():
        await bot.send_message(message.from_user.id, 'Ты че дурак что-ли? Тут нечего покупать. Не ну если хочешь закинь 50 рубасов на карту за старания)')
  
# --- Активные кнопки для выполнения запросов ---
        
@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == '⚠️Информация о боте':
        await bot.send_message(message.from_user.id, 'Привет! Я Assist бот для взаимодействия с ПК. С помощью моего функционала ты можешь: 1)Управлять работой ПК, 2)Делать скрины текущего положения экрана, 3)Управлять мультимедией.', reply_markup=key.mainMenu)

    elif message.text == '⬅️Главное меню':
        await bot.send_message(message.from_user.id, 'Главное меню', reply_markup=key.mainMenu)

    elif message.text == '⬅️Назад в функционал':
        await bot.send_message(message.from_user.id, 'Функционал', reply_markup=key.Funcmenu)

    elif message.text == '📝Возможности':
        await bot.send_message(message.from_user.id, 'Функции', reply_markup=key.Funcmenu)

    elif message.text == '📕Помощь':
        await bot.send_message(message.from_user.id, '/start-запуск бота, /buy-покупка подписки')

    elif message.text == '💰Подписка':
        await bot.send_message(message.from_user.id, "Подписка", reply_markup=key.Monmenu)

    elif message.text == 'Управление системой':
        await bot.send_message(message.from_user.id, 'Управление системой', reply_markup=key.pcmenu)

    elif message.text == 'Инфа о системе':
        await bot.send_message(message.from_user.id, 'Инфа', reply_markup=key.Infomenu)

    elif message.text == 'Управление процессами':
        await bot.send_message(message.from_user.id, 'Управление процессами', reply_markup=key.Processmenu)

    elif message.text == 'Звук':
        await bot.send_message(message.from_user.id, 'Данная функция находиться в разработке')

    # elif message.text == 'Изменить громкость':
    #     try:
    #      volume_value = float(message.text)
    #      if volume_value >= 0 and volume_value <= 100:
    #         devices = AudioUtilities.GetSpeakers()
    #         interface = devices.Activate(IAudioEndpointVolume._iid_, None)
    #         volume = cast(interface, POINTER(IAudioEndpointVolume))
    #         volume.SetMasterVolumeLevelScalar(volume_value / 100, None)
    #         await message.answer(f"Громкость изменена на {volume_value}%")
    #      else:
    #         await message.answer("Пожалуйста, введите значение от 0 до 100.")
    #     except ValueError:
    #         await message.answer("Пожалуйста, введите числовое значение.")
       
      ##  await bot.send_message(message.from_user.id, 'Введите значение аргумента, оно дожно быть от 0 до 100')
       # set_volume_check = False
       # if set_volume_check:
          #  if message.text.isdigit() and message.text != None:
          #   args = message.get_args()
          #   if args:
           #      Sound.volume_set(int(args))
           #      await message.answer(f'Громкость установлена на {str(args)} %')
           # else:
           #      await message.answer('Неправильная команда, укажите аргумент (0-100)')
        

    elif message.text == '⭐Запущенные процессы':
        #await bot.send_message(message.from_user.id, 'Процессы')
        proc_list = list(psutil.process_iter(['pid', 'name']))
        proc_list = proc_list[50:]
        text = ""
        for i, proc in enumerate(proc_list, start=1):
            text += f"{i}. {proc.info['name']}\n"
        await bot.send_message(message.from_user.id, text)

    elif message.text == '⛔Завершение процесса':
        await bot.send_message(message.from_user.id, 'Какой процесс вы хотите завершить?', reply_markup=key.Process2menu)

    elif message.text == 'Firefox':
        proc_name = 'firefox.exe'
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == proc_name:
                proc.terminate()
                await message.answer(f'Процесс {proc_name} успешно завершен!')
                break
        else:
            await message.answer(f'Процесс {proc_name} не найден.')

    elif message.text == 'Discord':
        proc_name = 'Update.exe'
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == proc_name:
                proc.terminate()
                await message.answer(f'Процесс {proc_name} успешно завершен!')
                break
        else:
            await message.answer(f'Процесс {proc_name} не найден.')

    elif message.text == 'Telegram':
        proc_name = 'Telegram.exe'      
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == proc_name:
                proc.terminate()
                await message.answer(f'Процесс {proc_name} успешно завершен!')
                break
        else:
            await message.answer(f'Процесс {proc_name} не найден.')

    elif message.text == 'Steam':
        proc_name = 'steam.exe'
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == proc_name:
                proc.terminate()
                await message.answer(f'Процесс {proc_name} успешно завершен!')
                break
        else:
            await message.answer(f'Процесс {proc_name} не найден.')
        
        
     
    elif message.text == '⚡Завершение работы ПК':
        popen("shutdown /s /t 0")
        await message.answer("✅Команда выполнена!")

    elif message.text == '📸Сделать скриншот экрана':
        image = pyautogui.screenshot()
        image.save("screenshot.png")
        with open('screenshot.png', 'rb') as photo:
            await bot.send_photo(message.from_user.id, photo, f"✅Команда выполнена!")
   
 
   
    # else:
    #    await message.reply('Неизвестная команда')


        




if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True) #Включение бота
