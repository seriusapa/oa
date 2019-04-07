import errno
import os
import sys
import tempfile

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests, json

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent,
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('XeCyvX9PLLCk74SS39QjZmFAbN+bX9w9/xKPNQUGb/QBTQAof5rwXEc3GepL49Pnduwc5YDuFV45gQqRxVt3Ibu1O4CgRbCNJU+lru5Rumj3UCxDLTdZ+WTGDe0miSP3pOC10BK8ryrK04dQ/E55lQdB04t89/1O/w1cDnyilFU=')
# Channel Secret NINO LIFF BOT
handler = WebhookHandler('492b626c089d6b3ee86f6040bd6de238')
#===========[ NOTE SAVER ]=======================
notes = {}
tokenz = {}

# Post Request
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(JoinEvent)
def handle_join(event):
    line_bot_api.reply_message(
        event.reply_token,[
                TextSendMessage(text='Makasih Udah Invite Saya, ini adalah Owner dari akun Ini'),
                TextSendMessage(text='https://www.instagram.com/aditiya230601')
        ])
    
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text
    
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text #simplify for receove message
    sender = event.source.user_id #get user_id
    gid = event.source.sender_id #get group_id
    
#=====[ LEAVE GROUP OR ROOM ]==========[ ARSYBAI ]======================
    if text == '/me':
        if isinstance(event.source, SourceUser):
            profile = line_bot_api.get_profile(event.source.user_id)
            line_bot_api.reply_message(
                event.reply_token, [
                    TextSendMessage(text='Display name: ' + profile.display_name),
                    TextSendMessage(text='Status message: ' + profile.status_message)
                ]
            )
        elif isinstance(event.source, SourceUser):
            profile = line_bot_api.get_profile(event.source.sender_id)
            line_bot_api.reply_message(
                event.reply_token, [
                    TextSendMessage(text='Display name: ' + profile.display_name),
                    TextSendMessage(text='Status message: ' + profile.status_message)
                ]
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't use profile in group chat"))

    if text == 'pamit':
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, [
                    TextSendMessage(text='Aku pamit ya, bye bye'),
                    TextSendMessage(text='https://www.instagram.com/aditiya230601')
                ])
            line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, [
                    TextSendMessage(text='aku pergi bye-bye'),
                    TextSendMessage(text='https://www.instagram.com/aditiya230601')
                ])
            line_bot_api.leave_room(event.source.room_id)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't leave from 1:1 chat"))
#=====[ TES MESSAGE ]=============[ ARSYBAI ]======================
    if text == "redtube on":
    	angka = random.randint(1, 200)
    	r = requests.get('https://api.boteater.vip/redtube?page={}'.format(angka))
    	data=r.text
    	data=json.loads(data)
    	for anu in data["result"]:
        	line_bot_api.reply_message(event.reply_token,VideoSendMessage(original_content_url=anu["dl"], preview_image_url=anu["img"]))
    elif text == "xvideos on":
    	angka = random.randint(1, 200)
    	r = requests.get('https://api.boteater.vip/xvideos?page={}'.format(angka))
    	data=r.text
    	data=json.loads(data)
    	for anu in data["result"]:
    		line_bot_api.reply_message(event.reply_token,VideoSendMessage(original_content_url=anu["dl"], preview_image_url=anu["img"]))
#=====[ TES MESSAGE ]=============[ ARSYBAI ]======================
    elif text == 'confirm':
        confirm_template = ConfirmTemplate(text='Bot nya bagus?', actions=[
            MessageTemplateAction(label='Yes', text='Yes!'),
            MessageTemplateAction(label='No', text='No!'),
        ])
        template_message = TemplateSendMessage(
            alt_text='Confirm alt text', template=confirm_template)
        line_bot_api.reply_message(event.reply_token, template_message)
    elif "/idline: " in event.message.text:
        skss = event.message.text.replace('/idline: ', '')
        sasa = "http://line.me/R/ti/p/~" + skss
        text_message = TextSendMessage(text=sasa)
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif "/artinama: " in event.message.text:
        skss = event.message.text.replace('/artinama: ', '')
        url = requests.get("https://rest.farzain.com/api/nama.php?&apikey=3w92e8nR5eWuDWQShRlh6C1ye&q="+ skss)
        data = url.json()
        text_message = TextSendMessage(text=data["result"])
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif "/zodiac: " in event.message.text:
        skss = event.message.text.replace('/zodiac: ', '')
        url = requests.get("https://triopekokbots026.herokuapp.com/zodiak="+ skss)
        data = url.json()
        text_message = TextSendMessage(text=data["result"])
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif "/tr-th: " in event.message.text:
        skss = event.message.text.replace('/tr-th: ', '')
        url = requests.get("https://api.tanyz.xyz/translateText/?&to=th&text="+ skss)
        data = url.json()
        text_message = TextSendMessage(text=data["Hasil"])
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif "/tr-en: " in event.message.text:
        skss = event.message.text.replace('/tr-en: ', '')
        url = requests.get("https://api.tanyz.xyz/translateText/?&to=en&text="+ skss)
        data = url.json()
        text_message = TextSendMessage(text=data["Hasil"])
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif "/tr-id: " in event.message.text:
        skss = event.message.text.replace('/tr-id: ', '')
        url = requests.get("https://api.tanyz.xyz/translateText/?&to=id&text="+ skss)
        data = url.json()
        text_message = TextSendMessage(text=data["Hasil"])
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
        
    elif "/fs1: " in event.message.text:
        skss = event.message.text.replace('/fs1: ', '')
        message = ImageSendMessage(
        original_content_url='https://rest.farzain.com/api/special/fansign/indo/viloid.php?apikey=rambu&text=' + skss,
        preview_image_url='https://rest.farzain.com/api/special/fansign/indo/viloid.php?apikey=rambu&text=' + skss
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/fs2: " in event.message.text:
        skss = event.message.text.replace('/fs2: ', '')
        message = ImageSendMessage(
        original_content_url='https://rest.farzain.com/api/special/fansign/cosplay/cosplay.php?apikey=rambu&text=' + skss,
        preview_image_url='https://rest.farzain.com/api/special/fansign/cosplay/cosplay.php?apikey=rambu&text=' + skss
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/graffiti: " in event.message.text:
        skss = event.message.text.replace('/graffiti: ', '')
        message = ImageSendMessage(
        original_content_url='https://rest.farzain.com/api/photofunia/graffiti_wall.php?&apikey=3w92e8nR5eWuDWQShRlh6C1ye&text2=Gans&text1=' + skss,
        preview_image_url='https://rest.farzain.com/api/photofunia/graffiti_wall.php?&apikey=3w92e8nR5eWuDWQShRlh6C1ye&text2=Gans&text1=' + skss
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/audio: " in event.message.text:
        skss = event.message.text.replace('/audio: ', '')
        message = AudioSendMessage(
        original_content_url=skss,
        duration=60000
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/video: " in event.message.text:
        skss = event.message.text.replace('/video: ', '')
        message = VideoSendMessage(
        original_content_url=skss,
        preview_image_url='https://i.ibb.co/GFWPRCV/1545946474474.jpg'
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/image: " in event.message.text:
        skss = event.message.text.replace('/image: ', '')
        message = ImageSendMessage(
        original_content_url=skss,
        preview_image_url='https://i.ibb.co/GFWPRCV/1545946474474.jpg'
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/linepost: " in event.message.text:
        skss = event.message.text.replace('/linepost: ', '')
        url = requests.get("https://rest.farzain.com/api/special/line.php?&apikey=vhbotsline&id="+ skss)
        data = url.json()
        message = VideoSendMessage(
        original_content_url=data["result"],
        preview_image_url='https://i.ibb.co/GFWPRCV/1545946474474.jpg'
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/youtubemp4: " in event.message.text:
        skss = event.message.text.replace('/youtubemp4: ', '')
        url = requests.get("https://api.tanyz.xyz/api/ytDown/?link="+ skss)
        data = url.json()
        message = VideoSendMessage(
        original_content_url=data["Hasil"]["urls"][0]["id"],
        preview_image_url='https://i.ibb.co/GFWPRCV/1545946474474.jpg'
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/youtubemp3: " in event.message.text:
        skss = event.message.text.replace('/youtubemp3: ', '')
        url = requests.get("https://rest.farzain.com/api/ytaudio.php?&apikey=rambu&id="+ skss)
        data = url.json()
        message = AudioSendMessage(
        original_content_url=data["result"]["webm"],
        duration=60000
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/smulevideo: " in event.message.text:
        skss = event.message.text.replace('/smulevideo: ', '')
        url = requests.get("https://api.eater.pw/smule?url="+ skss)
        data = url.json()
        message = VideoSendMessage(
        original_content_url=data["result"][0]["video"],
        preview_image_url=data["result"][0]["thumb"]
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/smuleaudio: " in event.message.text:
        skss = event.message.text.replace('/smuleaudio: ', '')
        url = requests.get("https://api.eater.pw/smule?url="+ skss)
        data = url.json()
        message = AudioSendMessage(
        original_content_url=data["result"][0]["video"],
        duration=60000
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/music: " in event.message.text:
        skss = event.message.text.replace('/music: ', '')
        url = requests.get("http://api.zicor.ooo/joox.php?song="+ skss)
        data = url.json()
        message = AudioSendMessage(
        original_content_url=data["url"],
        duration=240000
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/light: " in event.message.text:
        skss = event.message.text.replace('/light: ', '')
        url = requests.get("http://api.zicor.ooo/graffiti.php?text="+ skss)
        data = url.json()
        message = ImageSendMessage(
        original_content_url=data["image"],
        preview_image_url=data["image"]
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/street: " in event.message.text:
        skss = event.message.text.replace('/street: ', '')
        url = requests.get("http://api.zicor.ooo/streets.php?text="+ skss)
        data = url.json()
        message = ImageSendMessage(
        original_content_url=data["image"],
        preview_image_url=data["image"]
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/cookies: " in event.message.text:
        skss = event.message.text.replace('/cookies: ', '')
        url = requests.get("http://api.zicor.ooo/wcookies.php?text="+ skss)
        data = url.json()
        message = ImageSendMessage(
        original_content_url=data["image"],
        preview_image_url=data["image"]
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/sletters: " in event.message.text:
        skss = event.message.text.replace('/sletters: ', '')
        url = requests.get("http://api.zicor.ooo/sletters.php?text="+ skss)
        data = url.json()
        message = ImageSendMessage(
        original_content_url=data["image"],
        preview_image_url=data["image"]
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/goimage: " in event.message.text:
        skss = event.message.text.replace('/goimage: ', '')
        url = requests.get("https://api.eater.pw/googleimg?search="+ skss)
        data = url.json()
        message = ImageSendMessage(
        original_content_url=data["result"][0]["img"],
        preview_image_url=data["result"][0]["img"]
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0

    elif "/apakah " in event.message.text:
        quo = ('Iya','Tidak','Gak tau','Bisa jadi','Mungkin iya','Mungkin tidak')
        jwb = random.choice(quo)
        text_message = TextSendMessage(text=jwb)
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
        
    if text == '/tiktok':
        url = requests.get("https://rest.farzain.com/api/tiktok.php?country=jp&apikey=3w92e8nR5eWuDWQShRlh6C1ye&type=json")
        data = url.json()
        message = VideoSendMessage(
        original_content_url=data["first_video"],
        preview_image_url='https://i.ibb.co/GFWPRCV/1545946474474.jpg'
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/xvideos: " in event.message.text:
        skss = event.message.text.replace('/xvideos: ', '')
        url = requests.get("https://api.boteater.co/xvideos?page="+ skss)
        data = url.json()
        message = VideoSendMessage(
        original_content_url=data["result"][0]["dl"],
        preview_image_url='https://i.ibb.co/GFWPRCV/1545946474474.jpg'
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif (text == '/lokasi') or (text == 'Mylokasi'):
        message = LocationSendMessage(
        title='my location',
        address='Gg. Tentrem, Pasuruhan Lor, Jati, Kabupaten Kudus, Jawa Tengah 59349, Indonesia',
        latitude=-6.8172919,
        longitude=110.8217371
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == '/bmkg') or (text == 'Bmkg'):
        url = requests.get("https://api.tanyz.xyz/infoUpdateBMKG")
        data = url.json()
        message = TextSendMessage(text=data["Hasil"]["info"])
        line_bot_api.reply_message(event.reply_token, message)
#=============[ TOKEN ]=============[ ARSYBAI ]======================
    elif (text == '/chromeos') or (text == 'Chromeos'):
        url = requests.get("https://api.eater.pw/token?header=CHROMEOS")
        data = url.json()
        bsy = data['result'][0]['linktkn']
        bsyr = data['result'][0]['linkqr']
        tokenz[event.source.user_id]= bsy
        message = TextSendMessage(text='「 yudarea 」\nKlik Link Dibawah Ini Untuk Login Token Chrome\n'+bsyr+'\n\nketik /done untuk mendapatkan tokennya')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == '/iosipad') or (text == 'Iosipad'):
        url = requests.get("https://api.eater.pw/token?header=IOSIPAD")
        data = url.json()
        bsy = data['result'][0]['linktkn']
        bsyr = data['result'][0]['linkqr']
        tokenz[event.source.user_id]= bsy
        message = TextSendMessage(text='「 yudarea 」\nKlik Link Dibawah Ini Untuk Login Token Iosipad\n'+bsyr+'\n\nketik /done untuk mendapatkan tokennya')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == '/desktopmac') or (text == 'Desktopmac'):
        url = requests.get("https://api.eater.pw/token?header=DESKTOPMAC")
        data = url.json()
        bsy = data['result'][0]['linktkn']
        bsyr = data['result'][0]['linkqr']
        tokenz[event.source.user_id]= bsy
        message = TextSendMessage(text='「 yudarea 」\nKlik Link Dibawah Ini Untuk Login Token Desktopmac\n'+bsyr+'\n\nketik /done untuk mendapatkan tokennya')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == '/desktopwin') or (text == 'Desktopwin'):
        url = requests.get("https://api.eater.pw/token?header=DESKTOPWIN")
        data = url.json()
        bsy = data['result'][0]['linktkn']
        bsyr = data['result'][0]['linkqr']
        tokenz[event.source.user_id]= bsy
        message = TextSendMessage(text='「 yudarea 」\nKlik Link Dibawah Ini Untuk Login Token Desktopwin\n'+bsyr+'\n\nketik /done untuk mendapatkan tokennya')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == '/win10') or (text == 'Win10'):
        url = requests.get("https://api.eater.pw/token?header=WIN10")
        data = url.json()
        bsy = data['result'][0]['linktkn']
        bsyr = data['result'][0]['linkqr']
        tokenz[event.source.user_id]= bsy
        message = TextSendMessage(text='「 yudarea 」\nKlik Link Dibawah Ini Untuk Login Token Win10\n'+bsyr+'\n\nketik /done untuk mendapatkan tokennya')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == '/clova') or (text == 'Clova'):
        url = requests.get("https://api.eater.pw/token?header=CLOVAFRIENDS")
        data = url.json()
        bsy = data['result'][0]['linktkn']
        bsyr = data['result'][0]['linkqr']
        tokenz[event.source.user_id]= bsy
        message = TextSendMessage(text='「 yudarea 」\nKlik Link Dibawah Ini Untuk Login Token Clova\n'+bsyr+'\n\nketik /done untuk mendapatkan tokennya')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == '/done') or (text == 'Done'):
        data = tokenz[event.source.user_id]
        cok = requests.get(url = data)
        asu = cok.text
        message = TextSendMessage(text=asu)
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == '999+') or (text == '999++'):
        message = TextSendMessage(text='ckk by')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Bot') or (text == 'bot'):
        message = TextSendMessage(text='Siapa bot? ke bot an lu')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Tes') or (text == 'tes') or (text == 'Test') or (text == 'test'):
        message = TextSendMessage(text='suk beybeh')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Yudha') or (text == 'Yud') or (text == 'yud') or (text == 'yudha'):
        message = TextSendMessage(text='Apa manggil-manggil cogan')
        line_bot_api.reply_message(event.reply_token, message)
    elif text == '.':
        message = TextSendMessage(text='Titik titik amat so high lu')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Bah') or (text == 'bah'):
        message = TextSendMessage(text='Beh')
        line_bot_api.reply_message(event.reply_token, message)
#=====[ TEMPLATE MESSAGE ]=============[ ARSYBAI ]======================
    elif (text == '/help') or (text == 'help') or (text == 'Help'):
        buttons_template = TemplateSendMessage(
            alt_text='Help message',
            template=ButtonsTemplate(
                title='[ HELP MESSAGE ]',
                text= 'Tap the Button',
                actions=[
                    MessageTemplateAction(
                        label='My Creator',
                        text='/creator'
                    ),
                    MessageTemplateAction(
                        label='Media',
                        text='/media'
                    ),
                    MessageTemplateAction(
                        label='Musik',
                        text='/musik'
                    ),
                    MessageTemplateAction(
                        label='star bye',
                        text='starbye'
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token, buttons_template)
    elif text == '/media':
        buttons_template = TemplateSendMessage(
            alt_text='Media message',
            template=ButtonsTemplate(
                title='[ MEDIA MESSAGE ]',
                text= '>Tap the Button<',
                actions=[
                    MessageTemplateAction(
                        label='Media 1',
                        text='/media1'
                    ),
                    MessageTemplateAction(
                        label='Media 2',
                        text='/media2'
                    ),
                    MessageTemplateAction(
                        label='Token',
                        text='/listtoken'
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token, buttons_template)
    elif (text == '/media1') or (text == 'media1') or (text == 'Media1'):
        buttons_template = TemplateSendMessage(
            alt_text='Media area',
            template=ButtonsTemplate(
                title='MEDIA COMMAND',
                text= '>Tap the Button<',
                weight= "bold",
                align= 'center',
                actions=[
                    MessageTemplateAction(
                        label='Youtube',
                        text='≽ Use:\n• /youtubemp3:<link>\n• /youtubemp4:<link>'
                    ),
                    MessageTemplateAction(
                        label='Download Smule',
                        text='≽ Use:\n• /smuleaudio:<Link>\n• /smulevideo:<Link>'
                    ),
                    MessageTemplateAction(
                        label='Translate',
                        text='≽ Use:\n• /tr-id:<text>\n• /tr-en:<text>\n• /tr-th:<text>'
                    ),
                    MessageTemplateAction(
                        label='Info Bmkg',
                        text='≽ Use:\n• /bmkg'
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token, buttons_template)
        
    elif (text == '/media2') or (text == 'Media2') or (text == 'media2'):
        buttons_template = TemplateSendMessage(
            alt_text='media area',
            template=ButtonsTemplate(
                title='MEDIA COMMAND',
                text= '>Tap the Button<',
                weight= "bold",
                align= 'center',
                actions=[
                    MessageTemplateAction(
                        label='Image Text',
                        text='≽ Use:\n• /fs1:<Text>\n• /fs1:<Text>\n• /graffiti:<text>\n• /light:<text>\n• /street:<text>\n• /cookies:<text>\n• /sletters:<text>'
                    ),
                    MessageTemplateAction(
                        label='Zodiac',
                        text='≽ Use:\n• /zodiac: <text>'
                    ),
                    MessageTemplateAction(
                        label='Download Timeline',
                        text='≽ Use:\n• /linepost: <LinkTimeline>'
                    ),
                    MessageTemplateAction(
                        label='Checking',
                        text='≽ Use:\n• /audio:<link>\n• /video:<link>\n• /image:<link>'
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token, buttons_template)
#=====[ CAROUSEL MESSAGE ]==========[ ARSYBAI ]======================
    elif text == '/musik':
        buttons_template = TemplateSendMessage(
            alt_text='Enjoy whit music',
            template=ButtonsTemplate(
                title='[ GENDRE MUSIC ]',
                text= '>Tap the Button<',
                actions=[
                    MessageTemplateAction(
                        label='Music Indonesia',
                        text='/Mindo'
                    ),
                    MessageTemplateAction(
                        label='Music Barat',
                        text='/Mbarat'
                    ),
                    MessageTemplateAction(
                        label='Music Kpop',
                        text='/Mkpop'
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token, buttons_template)

    elif text == '/listtoken':
        message = TemplateSendMessage(
            alt_text='Token area',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        title='> LIST TOKEN <',
                        text='yudarea',
                        actions=[
                            MessageTemplateAction(
                                label='>Chromeos<',
                                text='/chromeos'
                            ),
                            MessageTemplateAction(
                                label='>Iosipad<',
                                text='/iosipad'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='> LIST TOKEN <',
                        text='yudarea',
                        actions=[
                            MessageTemplateAction(
                                label='>Desktopmac<',
                                text='/desktopmac'
                            ),
                            MessageTemplateAction(
                                label='>Desktopwin<',
                                text='/desktopwin'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='> LIST TOKEN <',
                        text='yudarea',
                        actions=[
                            MessageTemplateAction(
                                label='>Win10<',
                                text='/win10'
                            ),
                            MessageTemplateAction(
                                label='>Clova<',
                                text='/clova'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#=====[ CAROUSEL MESSAGE ]==========[ ARSYBAI ]======================
    elif (text == '/creator') or (text == 'About'):
        message = TemplateSendMessage(
            alt_text='>My creator<',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        title='Creator-PC',
                        text='This is my creator',
                        actions=[
                            URITemplateAction(
                                label='>BINTANG<',
                                uri='https://line.me/ti/p/~bintanga2'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='Creator-OA',
                        text='This is my creator',
                        actions=[
                            URITemplateAction(
                                label='>BINTANG<',
                                uri='https://line.me/ti/p/~bintanga2'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='My web',
                        text='Hehe',
                        actions=[
                            URITemplateAction(
                                label='>BINTANG<',
                                uri='https://line.me/ti/p/~bintanga2'
                            )
                        ]
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    if event.message.text == "/app clone":
        buttons_template = TemplateSendMessage(
            alt_text='App clone',
            template=ButtonsTemplate(
                title='Aplikasi clone',
                text='Klik salah satu menu dibawah ini.',
                thumbnail_image_url='https://imgur.com/Hbv4GWl.jpg',
                actions=[
                    URITemplateAction(
                        label='Parallel Space',
                        uri='https://play.google.com/store/apps/details?id=com.lbe.parallel.intl'
                    ),
                    URITemplateAction(
                        label='APP Cloner',
                        uri='https://play.google.com/store/apps/details?id=com.applisto.appcloner'
                    ),
                    URITemplateAction(
                        label='2Accounts',
                        uri='https://play.google.com/store/apps/details?id=com.excelliance.multiaccount'
                    ),
                    URITemplateAction(
                        label='Multi clone',
                        uri='https://play.google.com/store/apps/details?id=com.jumobile.multiapp'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
#=====[ FLEX MESSAGE ]==========[ ARSYBAI ]======================
    elif text == 'test':
        message = ImagemapSendMessage(
            base_url='https://i.imgur.com/g8P1V9Q.jpg',
            alt_text='manyimak corom',
            base_size=BaseSize(height=1040, width=1040),
            actions=[
                URIImagemapAction(
                    link_uri='https://line.me/ti/p/~bintanga2',
                    area=ImagemapArea(
                        x=0, y=0, width=520, height=1040
                    )
                ),
                MessageImagemapAction(
                    text='bintang ganteng',
                    area=ImagemapArea(
                        x=520, y=0, width=520, height=1040
                    )
                )
            ]
        )
        line_bot_api.reply_message(event.reply_token, message)

#=====[ Sticker MESSAGE ]==========[ ARSYBAI ]======================
    elif (text == 'anjir') or (text == 'Anjir'):
        message = TemplateSendMessage(
            alt_text='yudarea',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/16135443/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/~bintanga2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'astaghfirullah') or (text == 'Astaghfirullah'):
        message = TemplateSendMessage(
            alt_text='yudarea',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/16135442/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/~bintanga2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'sackid') or (text == 'Sackid'):
        message = TemplateSendMessage(
            alt_text='yudarea',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/15664374/IOS/sticker.png',
                        action=URIAction(uri='https://line.me/ti/p/~bintanga2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'kam') or (text == 'Kam'):
        message = TemplateSendMessage(
            alt_text='yudarea',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/51626494/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40ajd1759p')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Mantul') or (text == 'mantul') or (text == 'Mantap') or (text == 'mantap'):
        message = TemplateSendMessage(
            alt_text='yudarea',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/1072597/IOS/sticker.png',
                        action=URIAction(uri='http://line.me/ti/p/%40ajd1759p')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Wadaw') or (text == 'wadaw'):
        message = TemplateSendMessage(
            alt_text='yudarea',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/15671736/IOS/sticker.png',
                        action=URIAction(uri='http://line.me/ti/p/%40ajd1759p')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Hlh') or (text == 'hlh'):
        message = TemplateSendMessage(
            alt_text='yudarea',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/15708876/IOS/sticker.png',
                        action=URIAction(uri='http://line.me/ti/p/%40ajd1759p')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Huh') or (text == 'huh'):
        message = TemplateSendMessage(
            alt_text='yudarea',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/12690693/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40ajd1759p')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'kaget') or (text == 'Kaget'):
        message = TemplateSendMessage(
            alt_text='yudarea',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/49279761/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40ajd1759p')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Ngakak') or (text == 'ngakak'):
        message = TemplateSendMessage(
            alt_text='yudarea',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/73760360/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40ajd1759p')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'oksip') or (text == 'Oksip'):
        message = TemplateSendMessage(
            alt_text='yudarea',
            template=ImageCarouselTemplate(
              columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/52002735/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40ajd1759p')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'aw i cry') or (text == 'Aw i cry') or (text == 'Aw i cri') or (text == 'aw i cri'):
        message = TemplateSendMessage(
            alt_text='yudarea',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/19599278/IOS/sticker.png',
                        action=URIAction(uri='http://line.me/ti/p/%40ajd1759p')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'makasih') or (text == 'Makasih'):
        message = TemplateSendMessage(
            alt_text='yudarea',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/153453/IOS/sticker.png',
                        action=URIAction(uri='http://line.me/ti/p/%40ajd1759p')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'nyimak') or (text == 'Nyimak'):
        message = TemplateSendMessage(
            alt_text='yudarea',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/13162615/IOS/sticker.png',
                        action=URIAction(uri='http://line.me/ti/p/%40ajd1759p')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'ga') or (text == 'gak') or (text == 'gamau') or (text == 'Gamau') or (text == 'Ga') or (text == 'Gak'):
        message = TemplateSendMessage(
            alt_text='yudarea',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/8683557/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40ajd1759p')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'good night') or (text == 'Good night') or (text == 'selamat malam') or (text == 'Selamat malam'):
        message = TemplateSendMessage(
            alt_text='yudarea',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/8683546/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40ajd1759p')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'hai') or (text == 'Hai') or (text == 'halo') or (text == 'Halo'):
        message = TemplateSendMessage(
            alt_text='yudarea',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/52002738/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40ajd1759p')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'sabar') or (text == 'Sabar'):
        message = TemplateSendMessage(
            alt_text='yudarea',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/22499899/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40ajd1759p')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'wkwk') or (text == 'Wkwk'):
        message = TemplateSendMessage(
            alt_text='yudarea',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/27695296/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40ajd1759p')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'hehe') or (text == 'Hehe'):
        message = TemplateSendMessage(
            alt_text='yudarea',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/52002763/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40ajd1759p')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'siap') or (text == 'Siap'):
        message = TemplateSendMessage(
            alt_text='yudarea',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/51626520/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40ajd1759p')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif text == '?':
        message = TemplateSendMessage(
            alt_text='yudarea',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/34751035/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40ajd1759p')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'please') or (text == 'Please') or (text == 'tolong') or (text == 'Tolong'):
        message = TemplateSendMessage(
            alt_text='yudarea',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/51626499/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40ajd1759p')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'ok') or (text == 'oke') or (text == 'Ok') or (text == 'Oke'):
        message = TemplateSendMessage(
            alt_text='yudarea',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/51626500/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40ajd1759p')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'hahaha') or (text == 'Hahaha') or (text == 'Haha')or (text == 'haha'):
        message = TemplateSendMessage(
            alt_text='yudarea',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/40381622/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40ajd1759p')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'sebel') or (text == 'Sebel'):
        message = TemplateSendMessage(
            alt_text='yudarea',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/52114135/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40ajd1759p')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#=======================================================================================================================
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
