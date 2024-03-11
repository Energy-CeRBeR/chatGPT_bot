import g4f

providers = [provider for provider in g4f.Provider.__providers__ if provider.working]

for provider in providers:
    try:
        response = g4f.ChatCompletion.create(
            model="gpt"
        )