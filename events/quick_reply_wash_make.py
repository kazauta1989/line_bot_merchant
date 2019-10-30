from line_bot_api import *
from urllib.parse import parse_qsl


# 若前面選擇洗衣機，則會跳到這裡，讓使用者選擇是直立式或是滾筒式洗衣機

def quick_reply_wash_make_event(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
            text='您家中洗衣機廠牌為何？',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=PostbackAction(
                            label='國際牌（Panasonic）',
                            text='國際牌（Panasonic）',
                            data='make=234'
                        )
                    ),
                    QuickReplyButton(
                        action=PostbackAction(
                            label='國際牌（National）',
                            text='國際牌（National）',
                            data='make=456'
                        )
                    ),
                    QuickReplyButton(
                        action=PostbackAction(
                            label='惠而浦（Whirlpool）',
                            text='惠而浦（Whirlpool）',
                            data='make=789'
                        )
                    )
                ]
            )
        )
    )
