# programa que cria uma notificação no windows 10
# Feito por Matheus Nascimento Silva
# Data: 19/01/2023

#importando a biblioteca
from win10toast import ToastNotifier

#objeto do tipo ToastNotifier
toaster = ToastNotifier()
# Colocando as mensagens para as notificações
toaster.show_toast("Backup do NPEG!",
                   "Teste os sistemas internos!",
                   "Verifique os servidores!",
                   duration=10,
                   threaded=True)
while toaster.notification_active():True