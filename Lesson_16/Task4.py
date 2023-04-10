class CustomException(Exception):

    def __init__(self, msg):
        self.msg = msg
        with open('logs.txt', 'a') as file:
            file.write(f'An arror {msg} acquired\n')


try:
    raise CustomException('Something wrong')
except CustomException:
    print('done')

