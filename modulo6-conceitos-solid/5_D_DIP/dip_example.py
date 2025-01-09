'''
from .notificator_email import NotificatorEmail

# Estou fazendo uma forte dependência do clientService com o NotificationEmail
# A funcionalidade da classe está comprometida a esse notificator email
# ClientService = módulo de alto nível
class ClientService:
    def __init__(self, notificator: NotificatorEmail) -> None:
        self.notificator = notificator
    
    def send(self, message: str) -> None:
        self.notificator.send_notification(message)
'''

# # Correções na classe seguindo os princípios do DIP
from .notificator_interface import NotificatorInterface

class ClientService:
    def __init__(self, notificator: NotificatorInterface) -> None:
        self.notificator = notificator
    
    def send(self, message: str) -> None:
        self.notificator.send_notification(message)