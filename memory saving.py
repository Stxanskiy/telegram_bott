#короч решение проблемы с сжатием постов
import gzip
import telegram
import aiogram

bot = telegram.Bot(token = '5935810393:AAHjp8nGuO1vCSRSExH8gWWVYkiRDRim4no')

# Указываем сколько постов мы скачиваем с канала и пишем условие если в канале отсутсвует такое количество постов
post_number = 10
updates = bot.get_updates()

if len(updates)< post_number:
    posts = updates[-5:]
else:
    posts = updates[-post_number]


# Устанавливаем кодировку для сжатого файла
compress_text = gzip.compress(post_number.text.encode('utf-8'))
#Сжимаем фото в gzip
if post_number.photo:
    photo_file = post_number.photo[-1].get_file()
    compressed_photo = gzip.compress(photo_file.download_as_bytearray())
#Сжимаем видео в gzip
if post_number.video:
    video_file = post_number.video.get_file()
    compressed_video = gzip.compress(video_file.download_as_bytearray())
# блок для отправления сжатого файла
bot.share_document(chat_id = post_number.chat_id, document=compress_text, filename = 'compressed_text.gz')

if post_number.photo:
    bot.send_document(chat_id=post_number.chat_id, document=compressed_photo, filename = 'compressed_photo.gz')

if post_number.video:
    bot.send_document(chat_id=post_number.chat_id, document=compressed_video, filenamr= 'compressed_video.gz')
