import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

pr0fess0r_99=Client(
    "𝗕𝗼𝘁 𝗦𝘁𝗮𝗿𝘁𝗲𝗱 𝗣𝗹𝗲𝗮𝘀𝗲 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝗢𝗽𝘂𝘀𝗧𝗲𝗰𝗵𝘇",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

CHAT_ID=int(os.environ.get("CHAT_ID", None))
TEXT=os.environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nYour Auto Approved")
APPROVED = os.environ.get("APPROVED_WELCOME", "on").lower()

@pr0fess0r_99.on_message(filters.private & filters.command(["start"]))
async def start(client: pr0fess0r_99, message: Message):
    approvedbot = await client.get_me() 
    button=[[
      InlineKeyboardButton("𝚄𝙿𝙳𝙰𝚃𝙴𝚉", url="https://t.me/@TEAMTELEFLIXX"),
      InlineKeyboardButton("𝚂𝚄𝙿𝙿𝙾𝚁𝚃", url="https://t.me/+AdnOzGkxSo84NzVl")
      ],[
      InlineKeyboardButton("𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙱𝙴", url=f"https://t.me/mm_v3_bot")
      ]]
    await message.reply_text(text="**𝙷𝙴𝙻𝙻𝙾 {mention}...⚡\n\n𝙸 𝙰𝙼 𝙰 𝚂𝙸𝙼𝙿𝙻𝙴 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙰𝚄𝚃𝙾 𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙰𝙲𝙲𝙴𝙿𝚃 𝙱𝙾𝚃.\n𝙸 𝚌𝚊𝚗 𝚊𝚙𝚙𝚛𝚘𝚟𝚎 𝚞𝚜𝚎𝚛𝚜 𝚓𝚘𝚒𝚗 𝚁𝚎𝚚𝚞𝚎𝚜𝚝 𝚒𝚗 𝙶𝚛𝚘𝚞𝚙𝚜/𝙲𝚑𝚊𝚗𝚗𝚎𝚕𝚜... \n𝙸 𝚠𝚘𝚛𝚔 𝚏𝚘𝚛 @TEAMTELEFLIXX**", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@pr0fess0r_99.on_chat_join_request(filters.chat(CHAT_ID))
async def autoapprove(client: pr0fess0r_99, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} 𝙹𝙾𝙸𝙽𝙴𝙳 ⚡") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title))       

print("𝗕𝗼𝘁 𝗦𝘁𝗮𝗿𝘁𝗲𝗱 𝗣𝗹𝗲𝗮𝘀𝗲 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝗢𝗽𝘂𝘀𝗧𝗲𝗰𝗵𝘇")
pr0fess0r_99.run()
