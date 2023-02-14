from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
import Constants as keys
import json
import random
token = keys.API_KEY
bot = Bot(token)
dp = Dispatcher(bot)
X =  []
X2=[]
button1=InlineKeyboardButton(text="Guy",callback_data="Guy")
button2=InlineKeyboardButton(text="Osher",callback_data="Osher")
button3=InlineKeyboardButton(text="Max",callback_data="Max")
button4=InlineKeyboardButton(text="Noy",callback_data="Noy")
button5=InlineKeyboardButton(text="Omer",callback_data="Omer")
button6=InlineKeyboardButton(text="Ran",callback_data="Ran")
button7=InlineKeyboardButton(text="Gilad",callback_data="Gilad")
button8=InlineKeyboardButton(text="Michelle",callback_data="Michelle")
finish=InlineKeyboardButton(text="Finish",callback_data="Finish")

keyboard_inline = InlineKeyboardMarkup().add(button1).add(button2).add(button3).add(button4).add(button5).add(button6).add(button7).add(button8).add(finish)

@dp.callback_query_handler(text=["Finish"])
async def random_answer(message:types.Message):
    global X
    global X2
    zero=0
    one=0
    flag=True
    counter=0
    winner=""
    while flag:
        counter=counter+1
        for obj in X:
            print(obj)
            for k,v in obj.items():
                v=random.randint(0,1)
                obj[k]=random.randint(0,1)
                if v==0:
                    zero=zero+1
                else:
                    one=one+1
            to_dump={k:v}   
            X2.append(to_dump)
        print("x2",X2)
        print(counter,zero,one)
        X=X2
        X2=[]
        if (one+zero==len(X) and one ==1) or (one+zero==len(X) and zero ==1):
            flag=False
        else:
            zero=0
            one=0
        
    for obj in X:
        for k,v in obj.items():   
            if v==1 and one==1:
                print("key",k)
                winner=k
            elif v==0 and zero==1:
                print("key",k)
                winner=k
    await bot.send_message(keys.CHATID,f''' number of iterations is : {counter}
    {winner} you are the winner''')


@dp.message_handler(commands="start")
async def start(message: types.Message):
    global X
    global X2
    X=[]
    X2=[]
    await message.reply("Who are the participants?",reply_markup=keyboard_inline)

@dp.callback_query_handler(text=["Osher","Guy","Max","Noy","Omer","Ran","Gilad","Michelle"])
async def random_value(call:types.CallbackQuery):
    global X
    global X2
    flag=False
    to_dump={f'{call.data}':None}
    for obj in X:
        for k,v in obj.items():
            if k==call.data:
                flag=True
    if not flag:
        X.append(to_dump)
    flag=False
    print(len(X))
    print(json.dumps(X))
    await call.answer()

def main():
    executor.start_polling(dp)


if __name__=='__main__':
    main()