from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("بـدء استـخراج الجلسـة 🖥️", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="رجـوع 🔙", callback_data="home")],
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton(
                "𝗿𝘂𝗻𝘁𝗵𝗼𝗻 - سـورس رنثـون 🌐", url="https://t.me/xLxLxLrr"
            )
        ],
        [
            InlineKeyboardButton("كيفيـة الاستـخدام   ⍰ ", callback_data="help"),
            InlineKeyboardButton("حـول البـوت ℹ️", callback_data="about"),
        ],
        [InlineKeyboardButton("المطـور 👷", url="https://t.me/L_A_1")],
    ]

    START = """
**مرحبـًا 🙋** {}
━━━━━━━━━━━━━━━━━━
**- فـي البـوت الرسمـي التابـع لـ 𝗿𝘂𝗻𝘁𝗵𝗼𝗻** ⚙️🤖
**- يمكـنك اسـتخـراج جلسـة تيرمكـس وبايروجـرام لتنـصيب سـورس رنثـون
━━━━━━━━━━━━━━━━━━
**- قـم بالضغـط علـى بـدء استخـراج الجـلسـة ** 🛂
━━━━━━━━━━━━━━━━━━
**- ملاحظـات هامـة ** : -
**لا تقـم بطـرد الجلسـة التي اسمهـا Bit 64 لأنـك إذا طردتـها سيتوقـف تنصيبـك** 🚮
**احـذر مشاركـة الكود لأي شخـص لأنه يستطـيع اخـتراق حسابـك ** ⚠️
    """

    HELP = """
**أوامـر البـوت ⎙**
━━━━━━━━━━━━━━━━━
/about - لحول البوت ℹ️
/help - لمساعدتك ❓
/start - لبدء البوت ❗
/repo - لعرض معلومـات عـن السـورس 💡
/generate - لاستخراج الجلسات 👷
/cancel - لإلغاء الاستخراج 🥀
/restart - لترسيت البـوت ♻️
"""

    # About Message
    ABOUT = """
**حـول البـوت ⍰**

**هـذا البوت تـم تشـغيله بواسطـة 𝗿𝘂𝗻𝘁𝗵𝗼𝗻 و المـطور @L_A_1**

قنـاة السـورس 🖥️ : [𝗦𝗼𝘂𝗿𝗰𝗲 𝗿𝘂𝗻𝘁𝗵𝗼𝗻](https://t.me/xLxLxLrr)
لغـة البرمجـة ℹ️ : [بـايروجرام](docs.pyrogram.org)
اللغـة 🌐 : [بايثون](www.python.org)
المـطور 👷 : @L_A_1
    """

    # Repo Message
    REPO = """
━━━━━━━━━━━━━━━━━━━━━━━━
**سـورس رنثـون - 𝗿𝘂𝗻𝘁𝗵𝗼𝗻 **
**لا تنسـى الصـلاة على النبي 🤍 .**
┏━━━━━━━━━━━━━━━━━┓
⎆ سـورس رنثـون - 𝗿𝘂𝗻𝘁𝗵𝗼𝗻 . [اضـغط هـنا ❗](https://t.me/xLxLxLrr)
⎆ المطـور : [اضـغط هـنا ❗](https://t.me/L_A_1)
⎆ شـروحـات السـورس ℹ️ [اضـغط هـنا ❗](https://t.me/xLxLxLrr)
┗━━━━━━━━━━━━━━━━━┛ 
**تابـع لـ - 𝗿𝘂𝗻𝘁𝗵𝗼𝗻 🌐**
   """
