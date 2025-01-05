from abc import ABC, abstractmethod

# Essa classe define a regra de construção das demais classes que ela é implementada (herdada)
class NotificationSender(ABC):
    # Método abstrato, obriga que todas classes que herdarem NotificationSender, tenha o método send_notification presente nelas
    @abstractmethod
    def send_notification(self, message: str) -> None:
        pass

# Como está herdando NotificationSender, precisa implementar o send_notification, senão dará erro
class EmailNotificationSender(NotificationSender):
    def send_notification(self, message: str) -> None:
        print(f'Email message - {message}')

# Como está herdando NotificationSender, precisa implementar o send_notification, senão dará erro
class SMSNotificationSender(NotificationSender):
    def send_notification(self, message: str) -> None:
        print(f'SMS message - {message}')


# obj = NotificationSender()
# obj.send_notification("Hello, world!") - Isso não será executado, pois é um método abstrato, e ele serve apenas para ser herdado

obj = EmailNotificationSender()
obj.send_notification("Hello, world!")  # Output: Hello, world!

class Notificator:
    # Tipo do notification_sender é a classe que está obrigando a regra de construção
    # Ou seja, qualquer um que está implementando a classe de interface, serve para entrar na classe de Notificator
    # Se passar o SMSNotificationSender ou EmailNotificationSender, ambos irá funcionar
    # Esse método se chama injeção de dependência
    def __init__(self, notification_sender: NotificationSender) -> None:
        self.__notification_sender = notification_sender

    def send(self, message: str) -> None:
        self.__notification_sender.send_notification(message)

obj2 = Notificator(SMSNotificationSender())
obj2.send('Teste mensagem SMS')

obj3 = Notificator(EmailNotificationSender())
obj3.send('Teste mensagem Email')