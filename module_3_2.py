
recipient = input('Введите адрес получателя: ')
sender = input("Введите свой адрес: ")
def send_email(message, recipient, sender='university.help@gmail.com'):
    if (not (("@" in recipient) or (
            recipient.endswith(".com") or recipient.endswith(".ru") or recipient.endswith(".net")))
            or not (("@" in sender) or (sender.endswith(".com") or sender.endswith(".ru") or sender.endswith(".net")))):
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print('Письмо отправлено с адреса', sender, 'на адрес', recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)
    return recipient, sender

print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'))
print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'))
print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))


#if not '@' in recipient or recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net') or not '@' in sender or sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net'):

