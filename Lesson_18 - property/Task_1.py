# Створіть метод класу з іменем `validate`, який слід викликати з методу `__init__`
# для перевірки параметра email, переданого в конструктор. Логіка методу `validate`
# може полягати у перевірці того, чи переданий параметр email є дійсним рядком електронної пошти.

class Valid:
    def __init__(self, e_mail: str):
        self.e_mail = e_mail
        Valid.validate(self.e_mail)

    @classmethod
    def validate(cls, e_mail):
        if '..' in e_mail:
            raise ValueError('it should be a few simbols before and after "." ')
        j = 0
        c = 0
        for i in e_mail:
            if i == '@':
                j += 1
            if i == '"':
                c += 1
        if j > 1 or j < 1:
            raise ValueError('e-mail address should consist one "@"')
        if c == 2:
            left_part, middle, right_part = e_mail.split('"')
            if len(left_part) > 0 and len(left_part) > 0:
                if right_part[0] != '.':
                    raise ValueError('the simbols inside " " should be separated by "."')
                if left_part[-1] != '.':
                    raise ValueError('the simbols inside " " should be separated by "."')
            if ' ' in e_mail and ' ' not in middle or ' ' in left_part or ' ' in right_part:
                raise ValueError('the space is unacceptable in the e-mail addresses unless it inside the " "')
        else:
            if ' ' in e_mail:
                raise ValueError('the space is unacceptable in the e-mail addresses unless it inside the " "')
        local_part, domain_part = e_mail.split('@')
        if len(local_part) > 64:
            raise ValueError('local-part is longer than 64 characters')
        if "_" in domain_part:
            raise ValueError('Underscore is not allowed in domain part')


a = Valid('sentoaa@gmail.com')

