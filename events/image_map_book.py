from line_bot_api import *

# 此為Imagemap模板，選擇冷氣服務或是洗衣機服務


def book_event(event):
    line_bot_api.reply_message(
        event.reply_token,
        ImagemapSendMessage(
            base_url='https://i.imgur.com/P4DVQqS.png#',
            alt_text='訊息imagemap',
            base_size=BaseSize(height=700, width=1040),
            actions=[
                MessageImagemapAction(
                    text='洗衣機清潔',
                    area=ImagemapArea(
                        x=520, y=0, height=700, width=520
                    )
                ),
                MessageImagemapAction(
                    text='冷氣清潔',
                    area=ImagemapArea(
                        x=0, y=0, height=700, width=520
                    )
                )
            ]

        )
    )
