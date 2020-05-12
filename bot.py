# подключение библиотек
import discord
from discord.ext import commands
import random as rand
import config
import yandex_translate as ya
import requests
import json
from pathlib import Path
import asyncio
import OCR
import datetime


path = Path('users_langs.json')


# функция для проверки есть ли пользователь в json файле
def check_in_json(author_id, data):

    if author_id not in data['users'].keys():

        # добавление, если его нет
        data['users'][author_id] = "ru-en"
        path.write_text(json.dumps(data), encoding='utf-8')


# получние языков
langs = ya.get_langs()
# инвертирование словаря с языками
inv_langs = {value: key for key, value in langs.items()}

# создание бота
client = commands.Bot(command_prefix=config.BOT_PREFIX)
client.remove_command("help")


# при запуске бота:
@client.event
async def on_ready():

    # установка статуса боту
    await client.change_presence(activity=discord.Game(name=config.BOT_STATUS))

    print("Bot logged")


# сокращение команды what_lang
@client.command(pass_context=True)
async def wl(ctx, *text):

    await what_lang(ctx, *text)


# команда для определения языка на котором написан текст
@client.command(pass_context=True)
async def what_lang(ctx, *text):

    # получение отправителя команды
    author = ctx.message.author

    text = " ".join(text)

    # получнеие языка
    prob_lang = ya.what_lang_text(text)

    # отправка сообщения ботом
    await ctx.send(f'{author.mention}, вероятнее всего Ваш текст написан на языке "{langs[prob_lang]}"')

    print(f"{author} использует команду what_lang", datetime.datetime.now())


# сокращение команды bot_help
@client.command(pass_context=True)
async def h(ctx, command=None):

    await help(ctx, command)


# команда для получения помощи
@client.command(pass_context=True)
async def help(ctx, command=None):

    # получение отправителя команды
    author = ctx.message.author

    # создания вложения
    embed = discord.Embed(title="Команды бота Translator", colour=discord.Color.blue())
    # добавления картинки к вложению
    embed.set_thumbnail(url="https://sun1-85.userapi.com/f-V1PtohPctzBplrl-RwaqnRyXUZe8o1BXXiWw/7Y8vl5LwKFo.jpg")

    # если команда не задана
    if not command:

        # добавление подписи снизу
        embed.set_footer(text="Для подробной помощи !help (!h) {название_команды}\nПример: !help !set_lang")
        # добавление поля со списком команд
        embed.add_field(name=f"Команды - {len(config.COMMANDS)}", value="\n".join(config.COMMANDS))

        await ctx.send(f"{author.mention}, проверьте Ваши личные сообщения")

    # если команда не найдена
    elif command not in config.COMMANDS_CHECK:

        # добавление поля
        embed.add_field(name=command, value=f"Извините, я не знаю команды {command}")

    # если найдена
    else:

        # добавление подписи снизу
        embed.set_footer(text=config.COMMANDS_HELP[command]["footer"])
        # добавление поля с описанием команды
        embed.add_field(name=config.COMMANDS_HELP[command]["title"], value=config.COMMANDS_HELP[command]["value"])
        # добавление поля с использованием команды
        embed.add_field(name="Использование", value=config.COMMANDS_HELP[command]["usage"])

        if command == "!itr" or command == "!image_translate":

            # добавление картинки
            embed.set_image(url="https://sun1-24.userapi.com/jYhrdThtdjhFozTWbP9DE2PF69ergJlGOjKcKA/LmazQdpVYzo.jpg")

    # отправка вложения
    await ctx.author.send("Приятного использования!", embed=embed)

    print(f"{author} использует команду help", datetime.datetime.now())


# сокращение команды translate
@client.command(pass_context=True)
async def tr(ctx, *text):

    await translate(ctx, *text)


# команда для перевода текста
@client.command(pass_context=True)
async def translate(ctx, *text):

    # получение отправителя команды
    author = ctx.message.author
    # получение id отправителя команды
    author_id = str(author.id)
    # полчение содержимого json файла
    data = json.loads(path.read_text(encoding='utf-8'))

    # проверка пользователя в json файле
    check_in_json(author_id, data)

    # получение режима перевода пользователя
    lang = data['users'][author_id]
    prob_lang = ya.what_lang_text(text)

    text = " ".join(text)

    # первый язык
    first_lang = lang[:lang.find("-")]
    # второй язык
    second_lang = lang[lang.find("-") + 1:]

    # если язык не из режима перевода пользователя
    if prob_lang not in (first_lang, second_lang):

        # отправка сообщения ботом
        await ctx.send(f"""{author.mention}, извините, Ваш текст не похож ни на {langs[first_lang]}, \
ни на {langs[second_lang]}""")

        # завершение работы функции
        return

    # если режим перевода нужно переврнуть
    elif prob_lang == second_lang:

        # переворачивание режима перевода
        lang = f"{second_lang}-{first_lang}"

        first_lang, second_lang = second_lang, first_lang

    # получение перевода текста
    translated_text = ya.translate_text(text, lang)

    # отправка сообщения ботом
    await ctx.send(f'''{author.mention}, вот перевод Вашего текста c языка "{langs[first_lang]}" на \
{langs[second_lang]}: \n {translated_text}''')

    print(f"{author} использует команду translate", datetime.datetime.now())


# сокращение команды auto_translate
@client.command(pass_context=True)
async def atr(ctx, lang, *text):

    await auto_translate(ctx, lang, *text)


# команда для перевода текста с автоопределением языка
@client.command(pass_context=True)
async def auto_translate(ctx, lang, *text):

    # получение отправителя команды
    author = ctx.message.author

    text = " ".join(text)

    # первый язык
    first_lang = ya.what_lang_text(text)
    # если второй язык найден
    if lang.title() in inv_langs.keys():

        second_lang = inv_langs[lang.title()]

    # если не найден
    else:

        # отправка сообщения ботом
        await ctx.send(f"Извините, я не знаю язык {lang}, перевожу на русский")
        # выбор языка русский
        second_lang = "ru"

    if first_lang == second_lang:

        await ctx.send(f"{author.mention}, зачем переводить на один и тот же язык?")

        return

    # перевод языка в код
    lang = f"{first_lang}-{second_lang}"

    # получение перевода текста
    translated_text = ya.translate_text(text, lang)

    # отправка сообщения ботом
    await ctx.send(f'''{author.mention}, вот перевод Вашего текста c языка "{langs[first_lang]}" на \
{langs[second_lang]}: \n {translated_text}''')

    print(f"{author} использует команду auto_translate", datetime.datetime.now())


# сокращение команды image_translate
@client.command(pass_context=True)
async def itr(ctx, lang):

    await image_translate(ctx, lang)


# команда для перевода текста с изображения
@client.command(pass_context=True)
async def image_translate(ctx, lang):

    # получение отправителя команды
    author = ctx.message.author

    if lang.lower() == "ангглийский":

        await ctx.send(f"{author.mention}, зачем переводить на один и тот же язык?")

        return

    # обработка ошибок
    try:

        # доставание url из вложения
        url = str(ctx.message.attachments[0])
        url = url[url.find("url") + 5:url.rfind("'")]

    # если ошибка
    except:

        # отправка сообщения ботом
        await ctx.send(f"{author.mention}, извините, я не могу найти картинку")

    # если нет ошибок
    else:

        # запрос к функции перевода изображения в текст
        text = OCR.image_to_text(url)

        if not text:

            await ctx.send(f"{author.mention}, извините, я не смог найти текста на английском на картинке")

        else:

            print(f"{author} использует команду image_translate", datetime.datetime.now())

            # отправка текста в функции перевода с автоопределением языка
            await auto_translate(ctx, lang, text)


# сокращение команды set_lang
@client.command(pass_context=True)
async def sl(ctx, first_lang, second_lang):

    await set_lang(ctx, first_lang, second_lang)


# команда для смены режима перевода
@client.command(pass_context=True)
async def set_lang(ctx, first_lang, second_lang):

    # первый язык
    first_lang = first_lang.title()
    # второй язык
    second_lang = second_lang.title()
    # получение id отправителя команды
    author_id = str(ctx.message.author.id)
    # получение отправителя команды
    author = ctx.message.author
    # полчение содержимого json файла
    data = json.loads(path.read_text(encoding='utf-8'))

    check_in_json(author_id, data)

    # если оба языка не найдены
    if first_lang not in langs.values() and second_lang not in langs.values():

        # отправка сообщения ботом
        await ctx.send(f'{author.mention}, извините, я не знаю языка "{first_lang}" и языка "{second_lang}"')

    elif first_lang == second_lang:

        await ctx.send(f"{author.mention}, зачем переводить на один и тот же язык?")

        return

    # если первый язык не найден
    elif first_lang not in langs.values():

        # отправка сообщения ботом
        await ctx.send(f'{author.mention}, извините, я не знаю языка "{first_lang}"')

    # если второй язык не найден
    elif second_lang not in langs.values():

        # отправка сообщения ботом
        await ctx.send(f'{author.mention}, извините, я не знаю языка "{second_lang}"')

    # перевод языков в коды
    new_lang = f"{inv_langs[first_lang]}-{inv_langs[second_lang]}"
    # получение текущего языка пользователя из json файла
    cur_lang = data['users'][author_id]

    # если уже установлен этот режим
    if new_lang == cur_lang:

        # отправка сообщения ботом
        await ctx.send(f"{author.mention}, Ваш режим перевода уже установлен на {first_lang}->{second_lang}")

    else:

        # обработка ошибок
        try:

            # запись нового режима в json файл
            data['users'][author_id] = new_lang
            path.write_text(json.dumps(data), encoding='utf-8')

        # если ошибки
        except:

            # отправка сообщения ботом
            await ctx.send(f"{author.mention}, смена Вашего режима перевода завершилась неудачей")

        # если ошибок не было
        else:

            # отправка сообщения ботом
            await ctx.send(f"{author.mention}, Ваш режим перевода успешно сменён на {first_lang}-{second_lang}")

    print(f"{author} использует команду set_lang", datetime.datetime.now())


# сокращение команды current_mode
@client.command(pass_context=True)
async def cm(cxt):

    await current_mode(cxt)


# команда для получение текущего режима перевода
@client.command(pass_context=True)
async def current_mode(cxt):

    # получение отправителя команды
    author = cxt.message.author
    # получение id отправителя команды
    author_id = str(author.id)

    # полчение содержимого json файла
    data = json.loads(path.read_text(encoding='utf-8'))

    # проверка пользователья в json файле
    check_in_json(author_id, data)

    # получение режима перевода пользователя из json файла
    lang = data["users"][author_id]

    # первый язык
    first_lang = langs[lang[:lang.find("-")]]
    # второй язык
    second_lang = langs[lang[lang.find("-") + 1:]]

    # отправка сообщения ботом
    await cxt.send(f"{author.mention}, сейчас у Вас установлен режим перевода {first_lang}-{second_lang}")

    print(f"{author} использует команду current_mode")


@client.command(pass_context=True)
async def ll(cxt):

    await lang_list(cxt)


@client.command(pass_context=True)
async def lang_list(cxt):

    author = cxt.message.author

    text = "\n".join(inv_langs.keys())

    embed = discord.Embed(title="Поддерживаемые языки", colour=discord.Color.blue())

    embed.set_thumbnail(url="https://sun1-85.userapi.com/f-V1PtohPctzBplrl-RwaqnRyXUZe8o1BXXiWw/7Y8vl5LwKFo.jpg")

    embed.add_field(name="Языки", value=text)

    embed.set_footer(text="Приятного использования!")

    await cxt.author.send(embed=embed)

    await cxt.send(f"{author.mention}, проверьте Ваши личные сообщения")

# запуск бота
client.run(config.TOKEN)
