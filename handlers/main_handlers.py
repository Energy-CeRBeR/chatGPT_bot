import g4f

from copy import deepcopy

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from lexicon.lexicon import LEXICON, LEXICON_COMMANDS
from database.database import users_db, user_db_template
from servises.services import offset_history

router = Router()


@router.message(CommandStart())
async def start_bot(message: Message):
    await message.answer(text=LEXICON_COMMANDS[f"{message.text}"])
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy(user_db_template)


@router.message(Command(commands="help"))
async def help_info(message: Message):
    await message.answer(text=LEXICON_COMMANDS[f"{message.text}"])


@router.message(Command(commands='clear'))
async def process_clear_command(message: Message):
    user_id = message.from_user.id
    users_db[user_id]["conversation_history"] = []
    await message.reply(LEXICON["clear_history"])


@router.message()
async def request_handler(message: Message):
    user_id = message.from_user.id
    user_query = message.text

    if user_id not in users_db:
        await message.answer(LEXICON["not_in_database"])
        return

    users_db[message.from_user.id]["conversation_history"].append({"role": "user", "content": user_query})
    users_db[message.from_user.id]["conversation_history"] = offset_history(
        users_db[message.from_user.id]["conversation_history"]
    )
    chat_history = users_db[message.from_user.id]["conversation_history"]

    providers = [provider for provider in g4f.Provider.__providers__ if provider.working]

    chat_gpt_response = LEXICON["get_error"]
    for provider in providers:
        print(provider)
        try:
            response = await g4f.ChatCompletion.create_async(
                model=g4f.models.default,
                messages=chat_history,
                provider=provider,
            )
            chat_gpt_response = response
            if "[GoogleGenerativeAI Error]" in response or len(response) == 0:
                continue
            print(response)
            print(provider, "GOOD")
            break
        except Exception as e:
            print(f"{provider.__name__}:", e)
            chat_gpt_response = LEXICON["get_error"]

    users_db[message.from_user.id]["conversation_history"].append({"role": "assistant", "content": chat_gpt_response})

    print(users_db[message.from_user.id]["conversation_history"])
    length = sum(len(message["content"]) for message in users_db[message.from_user.id]["conversation_history"])
    print(length)

    await message.answer(chat_gpt_response)
