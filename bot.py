import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

# تعريف التوكن الخاص بالبوت
TOKEN = '7223794060:AAGrLXVMwtB0mB5lTTO_YcPP2iXPAoiidJA'

# إنشاء كائن البوت
bot = telepot.Bot(TOKEN)

# دالة لمعالجة الرسائل الواردة
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(f"Received: {content_type}, {chat_type}, {chat_id}")

    if content_type == 'text':
        if msg['text'] == '/start':
            # رسالة الترحيب عند بدء المحادثة
            first_name = msg['chat']['first_name'] if 'first_name' in msg['chat'] else ''
            welcome_message = f"👋 مرحباً {first_name} بك إلی عالم الأستثمار اظخط علی زر العربية ليظهر لك مزيد من ازرار لنأخذ جولة معا 😎 "
            keyboard = ReplyKeyboardMarkup(keyboard=[
                [KeyboardButton(text='العربية')],
            ], resize_keyboard=True)
            bot.sendMessage(chat_id, text=welcome_message, reply_markup=keyboard)

        elif msg['text'] == 'العربية':
            # القائمة العربية الرئيسية
            arabic_menu = ReplyKeyboardMarkup(keyboard=[
                [KeyboardButton(text='من نحن و كيف نعمل🥇')],
                [KeyboardButton(text='صناديق الأستثمار💼')],
                [KeyboardButton(text='الإداع و سحب 📥📤')],
                [KeyboardButton(text='الأرباح و سحبها🎯')],
                [KeyboardButton(text='الضمانات 100%')],
                [KeyboardButton(text='اعمال القادمة ➯')],
                [KeyboardButton(text='رجوع إلى القائمة الرئيسية')]
            ], resize_keyboard=True)
            bot.sendMessage(chat_id, "يرجى اختيار خيار من القائمة أدناه:", reply_markup=arabic_menu)

        elif msg['text'] == 'من نحن و كيف نعمل🥇':
            # رسالة من نحن و كيف نعمل
            about_message = (
             " نحن كشركة الكترونية للأستثمار ، نحن نعمل علی اساس التداول ( شراء و بيع ) عملات الرقمية مثل بتكوين و ايثريوم و ايضا عملات اخری....\n\n "
" عندما انت تستثمر معنا و تودع اموالك في صندوق ( A ) للأستثمار فلدينا فريق محترف في مجال التداول فهم سيتداولون بأموالك في عملات رقمية فعندما كانت صفقات مربحة فستتمكن من سحب ارباحك\n\n "
" لروئية معلومات اكثر حول الأرباح اذهب إلی زر الأرباح و سحبها🎯\n\n\n " 
" لأي استفسار و اسئلة تواصل معی 👇 @personal_supportcgbot \n\n "
"🔺 عندما تدخل في هاذا البوت و بعدها تظخط علی زر start البوت لن يرد عليك اكتب اسئلك و ارسل له سيرد عليك بأقرب وقت ممكن "
            )
            back_button = ReplyKeyboardMarkup(keyboard=[
                [KeyboardButton(text='رجوع إلى القائمة الرئيسية')]
            ], resize_keyboard=True)
            bot.sendMessage(chat_id, text=about_message, reply_markup=back_button)

        elif msg['text'] == 'صناديق الأستثمار💼':
            # رسالة صناديق الاستثمار
            investment_message = (
              " نحن نوفر صناديق استثمارية للأسباب التالية👇\n\n "
"① للأحتفاض علی سيولة استثمار\n"
"② يختلف صفقات صناديق من اخر\n"
"③ للترتيب عدد مستثمرين\n\n\n "

" الأن لدينا صندوق اول و واحد بأسم صندوق ( A ) قيمة إجمالية للأستثمار في هاذا صندوق 50,000$ و ايضا الحد الأدنی للأستثمار في هاذا صندوق 10$ و حد الأقصی لهاذا صندوق 1000$ و يتم تداول من عند فريقنا بأموال مستثمرة في هاذا صندوق اي شخص يستثمر معنا سيتم إضافة امواله في هاذا صندوق \n\n "
" للأستثمار في صندوق تواصل معی وكيلنا معتمد👇  @Cryptogolden_support "
            )
            back_button = ReplyKeyboardMarkup(keyboard=[
                [KeyboardButton(text='رجوع إلى القائمة الرئيسية')]
            ], resize_keyboard=True)
            bot.sendMessage(chat_id, text=investment_message, reply_markup=back_button)

        elif msg['text'] == 'الإداع و سحب 📥📤':
            # رسالة الإيداع والسحب
            deposit_withdrawal_message = (
                "للسحب و الإداع يأتي بطرق التالية 👇\n\n\n\n"


"للإداع: الطريقة رئيسية للإداع يتم عبر عملات رقمية العملات مقبولة يمكنك إداع اي عملة رقمية تريدها ان تودع معنا و لكن يجب ان يكون حد الأدنی بقيمة 10$ و حد الأقصی بقيمة 1000$\n "
"🔵\n"
"⚪\n"
"للسحب: يمكنك سحب ارباحك بطرق مختلفة كما يأتي للسحب 👇\n\n"
"① عملات رقمية \n"
"② فاستبي \n"
"③ زين كاش \n"
"④ باي بال\n"
"⑤ ويب موني\n"
"⑥ بيرفيكت موني\n"
"🔷\n"
"🔶\n"
"سحب راس مالك:  لسحب راس مالك المستثمر معنا يمكنك سحبها في اي وقت تريد و بأسرع وقت ممكن  و ايضا يمكنك سحب راس مالك المستثمر ف صندوق عبر جميع الطرق الذي ذكرناها في السحب\n\n"

"🔸🔹🔸🔹🔸🔹🔸🔹🔸\n\n"

"للأستثمار و سحب و الإداع تواصل معی وكيلنا المعتمد 👇 @Cryptogolden_support\n\n"

"لأي استفسار و اي اسئلة تواصل معی 👇 @personal_supportcgbot\n"

"🔺 عندما تدخل في هاذا البوت و بعدها تظخط علی زر start البوت لن يرد عليك اكتب اسئلك و ارسل له سيرد عليك بأقرب وقت ممكن "
            )
            back_button = ReplyKeyboardMarkup(keyboard=[
                [KeyboardButton(text='رجوع إلى القائمة الرئيسية')]
            ], resize_keyboard=True)
            bot.sendMessage(chat_id, text=deposit_withdrawal_message, reply_markup=back_button)

        elif msg['text'] == 'الأرباح و سحبها🎯':
            # رسالة الأرباح والسحب
            profits_message = (
                "للأرباح: عندما فريقنا يتداول في عملات رقمية و صفقات كانت ناجحة و ربحنا في صفقات سيتم تقسيم الأرباح كالتالي👇\n\n\n\n"
"20% سيتم حفضها في صندوق \n"
"30% سيكون للشركتنا \n"
"50% ملكك و يمكنك سحبها\n\n"
"✔✔✔✔✔✔\n\n"

"ال 20% يتم حفضها للأسباب متعددة منها إذا كانت خسرنا في صفقة ما فسنخر في راس مال فسنضيف هاذا ال 20% علی راس مالك للأحتفاض علی راس مالك ثابتا و يمكنك سحب هاذا ال 20% إذا كنت في حالة تريد ان توقف استثمار معنا فقط بهاذا الحالة يمكنك سحب ال 20% محفوضة\n\n\n"

"ال 30% إنها ملك للشركتنا و ملك لفريقنا لأننا نحن نعمل و نربح في صفقات فهاذا ال 30% للشركتنا\n\n\n"

"ال 50% إنها ملكك و يمكنك سحبها في اي وقت تريد\n\n\n"

"إذا كنت لن تفهم عن النسبة 20% و 30% و 50% انظر لهاذا المثال👇\n\n"
"للمثال انت استثمرت معنا بقيمة 1000$  و فريقنا يتداول بهاذا اموال لمدة يومين و كانت نتيجة صفقات مربحة و مجموع الربح كانت 100$  فسيتم تقسيم هاذه ارباح 20$ سيتم حفضها في صندوق هاذا هو ال 20%  و 30$ إنها سيكون ملكنا هاذا هو ال 30% و ال 50$ سيكون ملكك و يمكنك سحبها في اي وقت تريد هاذا هو ال 50% و راس مالك سيتكون مثلما كما هو سيكون 1000$ \n\n"

"🔷🔶🔷🔶🔷🔶🔷🔶\n\n"

"و ايضا يمكنك سحب ارباحك في اي وقت تريد و بأسرع وقت ممكن و ايضا يمكنك سحب راس مالك المستثمر\n\n"
"🔻 لا تنسی ادخل إلی قناتنا تلجرام لرؤية نسبة ارباح صفقات و ايضا لرؤية تحديثات الجديدة  https://t.me/cryptog0lden\n\n"

"⬆⬇⬆⬇⬆⬇⬆⬇⬆⬇⬆⬇⬆⬇⬆⬇⬆\n\n"


"للأستثمار ، سحب ، إداع تواصل معی وكيلنا المعتدم 👇 @Cryptogolden_support\n\n"
"🔸\n"
"للأستفسار او اي اسئلة يرجي تواصل معی👇 @personal_supportcgbot\n"
"🔺 عندما تدخل في هاذا البوت و بعدها تظخط علی زر start البوت لن يرد عليك اكتب اسئلك و ارسل له سيرد عليك بأقرب وقت ممكن "
            )
            back_button = ReplyKeyboardMarkup(keyboard=[
                [KeyboardButton(text='رجوع إلى القائمة الرئيسية')]
            ], resize_keyboard=True)
            bot.sendMessage(chat_id, text=profits_message, reply_markup=back_button)

        elif msg['text'] == 'الضمانات 100%':
            # رسالة الضمانات
            guarantee_message = (
                "نحن نعطيك ضمانات للأحتفاض علی راس مالك مستثمر معنا ان يكون ثابتا و لن تخسر من راس مالك ، و ايضا السرعة في سحب و الإداع و ايضا الأستمرارية في العمل و جني الأرباح \n\n"
"🔷\n"
"🔶\n"
"🔷\n\n"

"للأستثمار ، سحب ، إداع، تواصل معی وكيلنا المعتدم  @Cryptogolden_support\n"
"🔸\n"
"للأستفسار او اي اسئلة يرجي تواصل معی @personal_supportcgbot\n"
"🔺 عندما تدخل في هاذا البوت و بعدها تظخط علی زر start البوت لن يرد عليك اكتب اسئلك و ارسل له سيرد عليك بأقرب وقت ممكن "
            )
            back_button = ReplyKeyboardMarkup(keyboard=[
                [KeyboardButton(text='رجوع إلى القائمة الرئيسية')]
            ], resize_keyboard=True)
            bot.sendMessage(chat_id, text=guarantee_message, reply_markup=back_button)

        elif msg['text'] == 'اعمال القادمة ➯':
            # رسالة الأعمال القادمة
            upcoming_projects_message = (
                "يوجد لدينا اعمال القادمة👇\n\n\n"
"- إنشاء موقع الكتروني للشركة ، تحت تنفيذ\n"
"- السحب و إداع مباشر ، تحت تنفيذ\n"
"- عملة رقمية للشركة ، تحت تنفيذ\n"
"🔷\n"
"🔶\n"

"للأستثمار ، سحب ، إداع، تواصل معی وكيلنا المعتدم 👇 @Cryptogolden_support\n"
"🔸\n"
"للأستفسار او اي اسئلة يرجي تواصل معی👇 @personal_supportcgbot\n"
"🔺 عندما تدخل في هاذا البوت و بعدها تظخط علی زر start البوت لن يرد عليك اكتب اسئلك و ارسل له سيرد عليك بأقرب وقت ممكن "
            )
            back_button = ReplyKeyboardMarkup(keyboard=[
                [KeyboardButton(text='رجوع إلى القائمة الرئيسية')]
            ], resize_keyboard=True)
            bot.sendMessage(chat_id, text=upcoming_projects_message, reply_markup=back_button)

        elif msg['text'] == 'رجوع إلى القائمة الرئيسية':
            # رسالة الرجوع إلى القائمة الرئيسية
            back_to_main_menu_message = "أهلاً بك مجدداً في القائمة الرئيسية.\nيرجى اختيار خيار من القائمة أدناه:"
            main_menu = ReplyKeyboardMarkup(keyboard=[
                [KeyboardButton(text='من نحن و كيف نعمل🥇')],
                [KeyboardButton(text='صناديق الأستثمار💼')],
                [KeyboardButton(text='الإداع و سحب 📥📤')],
                [KeyboardButton(text='الأرباح و سحبها🎯')],
                [KeyboardButton(text='الضمانات 100%')],
                [KeyboardButton(text='اعمال القادمة ➯')],
            ], resize_keyboard=True)
            bot.sendMessage(chat_id, text=back_to_main_menu_message, reply_markup=main_menu)

# استخدام تابع البوت لمعالجة الرسائل
bot.message_loop(handle)

# البقاء في حالة تشغيل للبوت
print('Listening...')
while True:
    pass
