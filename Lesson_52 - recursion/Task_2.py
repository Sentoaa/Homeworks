
def is_palindrome(looking_str: str, index: int = 0) -> bool:
    # якщо довжина рядка менше або дорівнює 1, то рядок є паліндромом
    if len(looking_str) <= 1:
        return True
    # перевіряємо, чи співпадають перший і останній символи рядка
    if looking_str[index] == looking_str[-1]:
        # якщо так, викликаємо функцію рекурсивно зі зменшеним рядком
        return is_palindrome(looking_str[index + 1:-1])
    else:
        # якщо ні, рядок не є паліндромом
        return False

print(is_palindrome('mom'))
print(is_palindrome('sassas'))
print(is_palindrome('o'))

