import os

import speech_recognition as sr
import keyboard

recognizer = sr.Recognizer()

def handle_command(text):
    text = text.lower()

    if "финик" in text:
        print("Команда:", text)


        if "следующая" in text or "дальше" in text:
            print("⏭ Следующая")
            keyboard.press_and_release("next track")


        elif "назад" in text or "предыдущая" in text:
            print("⏮ Назад")
            keyboard.press_and_release("previous track")


        elif "стоп" in text:
            print("⏸ Стоп")
            keyboard.press_and_release("play/pause")


        elif "плей" in text or "продолжи" in text:
            print("▶ Плей")
            keyboard.press_and_release("play/pause")

        elif "выключи компьютер" in text or "выключи пк" in text:
            print("💻 Выключаю компьютер...")
            os.system("shutdown /s /t 0")


def listen():
    with sr.Microphone() as source:
        print("Слушаю...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        print("Ты сказал:", text)
        handle_command(text)

    except sr.UnknownValueError:
        print("Не понял 😅")

    except sr.RequestError:
        print("Ошибка сервиса распознавания")



while True:
    listen()