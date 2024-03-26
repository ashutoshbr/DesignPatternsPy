from abc import ABC, abstractmethod


class EmailService(ABC):
    @abstractmethod
    def send_email(self, content: str):
        pass


class Service1(EmailService):
    def send_email(self, content: str):
        print(f"Service 1\n{content}")


class Service2(EmailService):
    def send_email(self, content: str):
        print(f"Service 2\n{content}")


class EmailSender:
    def __init__(self, email_service: EmailService = Service1()) -> None:
        self.email_service = email_service

    def send_email(self, content: str):
        return self.email_service.send_email(content)


email_service = Service2()
sender = EmailSender(email_service=email_service)
sender.send_email("Hello, This is the content.")
