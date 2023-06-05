from telebot import TeleBot
import cv2 as cv
import platform
import numpy as np
import os
from dotenv import dotenv_values
from darknet.darknet import *

# config = dotenv_values('.env')

token = os.environ['TOKEN_TG']
bot = TeleBot(token)


network, class_names, class_colors = load_network("darknet/cfg/yolov4-csp.cfg", "darknet/cfg/coco.data",
                                                   "darknet/yolov4-csp.weights")
width = network_width(network)
height = network_height(network)

def darknet_helper(img, width, height):
    darknet_image = make_image(width, height, 3)
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img_resized = cv.resize(img_rgb, (width, height),
                                interpolation=cv.INTER_LINEAR)

    img_height, img_width, _ = img.shape
    width_ratio = img_width/width
    height_ratio = img_height/height

    copy_image_from_bytes(darknet_image, img_resized.tobytes())
    detections = detect_image(network, class_names, darknet_image)
    free_image(darknet_image)
    return detections, width_ratio, height_ratio


@bot.message_handler(commands=['start'])
def incoming(message):
    bot.reply_to(message, f'Hello! And Welcome {message.from_user.first_name}')
    bot.send_message(message.chat.id, '<i>You can use /help command</i>', parse_mode='HTML', disable_web_page_preview=True)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.reply_to(message, '<i>Please load image! And I can detected object on it!</i>', 
                 parse_mode='HTML', disable_web_page_preview=True)
    bot.send_message(chat_id=message.chat.id, text=f'Your chat id {message.chat.id}')

@bot.message_handler(content_types=['photo'])
def get_image(message):
    bot.send_message(message.chat.id, '<i>Get file..</i>', parse_mode='HTML', disable_web_page_preview=True)
    
    file_path = bot.get_file(message.photo[-1].file_id)

    print(os.path.abspath(os.curdir))
    file_d = bot.download_file(file_path.file_path)
    dir_f = os.path.abspath(os.curdir)
    if platform.system() == 'Windows':
        file_s_path = f'{dir_f}\\img\\{file_path.file_unique_id}.jpg'
    else:
        file_s_path = f'{dir_f}/img/{file_path.file_unique_id}.jpg'
    
    with open(f'log.txt', 'a+') as log_file:
        log_file.write('-------------------------------********************-----------------------------\n')
        log_file.write(f'Get fie from user:{message.from_user.id}_{message.from_user.first_name}_{message.from_user.last_name}: nikname:{message.from_user.username}\n')
        log_file.write(f'File data: id-{file_path.file_unique_id}:size-{file_path.file_size}: path-{file_path.file_path}\n')
    with open(file_s_path, 'wb') as new_file:
            new_file.write(file_d)
    image = cv.imread(file_s_path, cv.IMREAD_COLOR)

    detections, width_ratio, height_ratio = darknet_helper(image, width, height)    
    print(detections)
    
    bot.send_message(message.chat.id, '<i>Please wait a litlle... I\'m almost Done :)</i>', parse_mode='HTML', disable_web_page_preview=True)
    for label, confidence, bbox in detections:
        left, top, right, bottom = bbox2points(bbox)
        left, top, right, bottom = int(left * width_ratio), int(top * height_ratio), int(right * width_ratio), int(bottom * height_ratio)
        cv.rectangle(image, (left, top), (right, bottom), class_colors[label], 2)
        cv.putText(image, "{} [{:.2f}]".format(label, float(confidence)),
                            (left, top - 5), cv.FONT_HERSHEY_SIMPLEX, 0.5,
                            class_colors[label], 2)
    file_s_path = f'{dir_f}/img/{file_path.file_unique_id}-D.jpg'
    cv.imwrite(file_s_path, image)

    with open(file_s_path, 'rb') as f:
          img_s = f.read()
    

    bot.send_photo(message.chat.id, img_s, caption='Thank you for Testing!!!')
    print('File send to user...')
    

bot.infinity_polling()
