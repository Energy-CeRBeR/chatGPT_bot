import asyncio

import g4f


def offset_history(history, max_length=4096):
    current_length = sum(len(message["content"]) for message in history)
    while history and current_length > max_length:
        removed_message = history.pop(0)
        current_length -= len(removed_message["content"])
    return history


async def process():
    conversation_history = list()
    user_query = "start"
    while user_query != "break":
        user_query = input("Введите ваш запрос: ")
        conversation_history.append({"role": "user", "content": user_query})
        conversation_history = offset_history(conversation_history)
        chat_history = conversation_history

        providers = [provider for provider in g4f.Provider.__providers__ if provider.working]
        chat_gpt_response = "error"
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
                print(provider, "GOOD")
                break
            except Exception as e:
                print(f"{provider.__name__}:", e)
                chat_gpt_response = "error"

        conversation_history.append({"role": "assistant", "content": chat_gpt_response})

        print(conversation_history)
        print(chat_gpt_response)


if __name__ == "__main__":
    asyncio.run(process())


