LEXICON: dict[str, str] = {
    '/start': '<b>Привет, читатель!</b>\n\nЭто бот, в котором '
              'ты можешь прочитать книгу Рэя Брэдбери "Марсианские '
              'хроники"\n\nЧтобы посмотреть список доступных '
              'команд - набери /help',
    '/help': '<b>Это бот-читалка</b>\n\nДоступные команды:\n\n/beginning - '
             'перейти в начало книги\n/continue - продолжить '
             'чтение\n/bookmarks - посмотреть список закладок\n''/to_page <b>номер страницы</b> - '
             'перейти на определённую страницу\n''/help - '
             'справка по работе бота\n\nЧтобы сохранить закладку - '
             'нажмите на кнопку с номером страницы\n\n<b>Приятного чтения!</b>',
    'clear_history': 'История вашего диалога с ботом очищена!',
    'not_in_database': 'Извините, но Вас нет в нашей базе данных.\n'
                       ' Для начала работы с ботом напишите команду /start',
    "get_error": "Извините, по вашему запросу произошла ошибка!",
    '/bookmarks': '<b>Это список ваших закладок:</b>',
    'edit_bookmarks': '<b>Редактировать закладки</b>',
    'edit_bookmarks_button': '❌ РЕДАКТИРОВАТЬ',
    'del': '❌',
    'cancel': 'ОТМЕНИТЬ',
    'no_bookmarks': 'У вас пока нет ни одной закладки.\n\nЧтобы '
                    'добавить страницу в закладки - во время чтения '
                    'книги нажмите на кнопку с номером этой '
                    'страницы\n\n/continue - продолжить чтение',
    'cancel_text': '/continue - продолжить чтение'
}

LEXICON_COMMANDS: dict[str] = {
    '/start': 'Привет, это CeRBeR_GPT!\n'
              'Я стану твоим лучшим помощником и отвечу на любой вопрос!\n'
              '/help для просмотра подробной информации',
    '/help': 'Доступные команды:\n '
             '/clear - Очистить диалог с ботом\n'
             'Для начала работы с помощником, просто отправьте ему сообщение с вашим запросом'
}
