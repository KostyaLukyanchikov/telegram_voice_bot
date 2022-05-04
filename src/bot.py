import io
from typing import Optional

import gtts
import gtts.lang
from telegram import Update
from telegram.ext import Updater, CallbackContext, MessageHandler, Filters

import config
import lang_detector
import specials


def run():
    start_bot()


def start_bot():
    updater = Updater(config.TOKEN)
    voicy = MessageHandler(
        filters=Filters.text & (~Filters.command) & (~Filters.forwarded),
        callback=voice_reply
    )
    updater.dispatcher.add_handler(voicy)
    updater.start_polling()


def voice_reply(update: Update, context: CallbackContext):
    username = update.effective_message.from_user.username
    special_answer = get_special_answer(username)

    context.bot.send_voice(
        chat_id=update.effective_chat.id,
        reply_to_message_id=update.message.message_id,
        voice=get_speech(special_answer or update.message.text)
    )


def get_special_answer(username: str) -> Optional[str]:
    return specials.ANSWERS_BY_USERS.get(username)


def get_speech(text: str):
    lang = lang_detector.detect_lang(text)
    speech = gtts.gTTS(text=text, lang=lang, lang_check=False)
    buffer = io.BytesIO()
    speech.write_to_fp(buffer)
    buffer.seek(0)
    return buffer
