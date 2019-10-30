from line_bot_api import *


# 若前面選擇洗衣機，則會跳到這裡，讓使用者選擇是直立式或是滾筒式洗衣機

def quick_reply_wash_action_event(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
            text='您家中洗衣機為以下何種類型？？',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=PostbackAction(
                            label='直立式洗衣機（開口朝上) ',
                            text='直立式洗衣機（開口朝上) ',
                            data='action=upright'
                        )
                    ),
                    QuickReplyButton(
                        action=PostbackAction(
                            label='滾筒式洗衣機（開口朝前）',
                            text='滾筒式洗衣機（開口朝前）',
                            data='action=roller'
                        )
                    )
                ]
            )
        )
    )
