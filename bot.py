import os                     # traz o módulo do sistema. Usado pra os.getenv
from dotenv import load_dotenv    # traz só a função que lê o arquivo .env
from telegram import Update         #Update oque aconteceu (mensagem,clique,etc )   
from telegram.ext import ApplicationBuilder,CommandHandler,ContextTypes # traz o construtor do bot
from telegram import InlineKeyboardButton,InlineKeyboardMarkup # classes do buton e teclado
from telegram.ext import ApplicationBuilder,CommandHandler,CallbackQueryHandler,ContextTypes  # pega a função de clique na biblioteca 

load_dotenv() #carrega  o .env
TOKEN = os.getenv("TELEGRAM_TOKEN") #pega o token  do ambiente e guarda na variavel TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):# função que roda no /start. async = pode usar await
  teclado =[                                                      #lista de listas = cada lista interna é uma linha de botoẽos 
     [InlineKeyboardButton("Agendar", callback_data="agendar")],  #botão visivel "Agendar"; callback_data é o codigo ue o bot recebe quando clicado 
     [InlineKeyboardButton("Horarios",callback_data="horarios")],  
     [InlineKeyboardButton("Serviços", callback_data="servicos")]
  ]
  await update.message.reply_text(  # responde a mensagem com o teclado anexado. await = espera sem  travar.
     "Fala! O que você deseja?",
     reply_markup= InlineKeyboardMarkup(teclado), 
  )


async def botao(update: Update, contetxt: ContextTypes.DEFAULT_TYPE):
   consulta = update.callback_query  # é o "toque" que chegou. ele guarda. tudo sobre o botão 
   await consulta.answer()  # avisa o Telegramm "recebi o toque" sem ele, o botão fica com um relogio girando
   if consulta.data =="servicos":  #
      await consulta.edit_message_text("Corte - R$ 30\nBarba - 50   ")

   elif consulta.data == "horarios":
      await consulta.edit_message_text("16:00   18:00")

   elif consulta.data== "agendar":
     await consulta.edit_message_text("DIA 1, DIA 2 , DIA 7, DIA 9")

#async def servico (update: Update, context: ContextTypes.DEFAULT_TYPE): #função que roda no /serviço; \n= quebra de linha.
#   await update.message.reply_text("Corte - R$ 30\nBarba - 50  ")

app = ApplicationBuilder().token(TOKEN).build()   # cria o bot usando o token
app.add_handler(CommandHandler("start", start))    # quando chama  /start, chama start "
app.add_handler(CallbackQueryHandler(botao))   # chama a função do botão
app.run_polling ()             # liga  o bot. fica perguntando ao Telegram se há novidades(loop infinito).

