import telegram
import asyncio

def send_telegram(photo_path="alert.png"):
    try:
        my_token = "7133644881:AAF_r7iaaYcho-DkDnu3J6je3O7Ph_4bDGM"
        bot = telegram.Bot(token=my_token)
        # Tạo và chạy một coroutine object
        asyncio.run(
            bot.send_photo(chat_id = "6794868613", photo=open(photo_path, "rb"), caption="Có xâm nhập, nguy hiêm!"))

    except Exception as ex:
        print("Can not send message telegram ", ex)

    print("Send success")
