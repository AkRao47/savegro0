import os
from .. import bot as savegroot
from telethon import events, Button
from telethon.tl.types import InputMediaPhoto

S = "/start"
START_PIC = "groot welcome.jpg"
TEXT = "👋 Hi, This is 'Paid Restricted Content Saver' bot Made by __**Save Groot**__ only for you.\n\n✅ Send me the Link of any message of Restricted Channels to Clone it here.\nFor private channel's messages, send the Invite Link first."

def is_set_button(data):
    return data == "set"

def is_rem_button(data):
    return data == "rem"

@savegroot.on(events.CallbackQuery(pattern=b"set"))
async def sett(event):    
    savegroot = event.client
    button = await event.get_message()
    msg = await button.get_reply_message()
    await event.delete()
    async with savegroot.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("Send me any image for thumbnail as a `reply` to this message.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
            return
        mime = x.file.mime_type
        if 'png' not in mime and 'jpg' not in mime and 'jpeg' not in mime:
            return await xx.edit("No image found.")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Trying.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("Temporary thumbnail saved!")

@savegroot.on(events.CallbackQuery(pattern=b"rem"))
async def remt(event):  
    savegroot = event.client            
    await event.edit('Trying... to save Bamby ... Wait')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('Removed!')
    except Exception:
        await event.edit("No thumbnail saved.")                        

@savegroot.on(events.NewMessage(pattern=f"^{S}"))
async def start_command(event):
    # Creating inline keyboard with buttons
    buttons = [
        [Button.inline("SET THUMB", data="set"),
         Button.inline("REM THUMB", data="rem")],
        [Button.url("Join Channel", url="t.me/savegroot")],
        [Button.url("For /batch command contact us", url="https://t.me/savegroot_bot")]
    ]

    # Sending photo with caption and buttons
    await savegroot.send_file(
        event.chat_id,
        file=START_PIC,
        caption=TEXT,
        buttons=buttons
    )
