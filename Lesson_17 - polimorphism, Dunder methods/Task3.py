class Fraction:

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
        if self.number2 == 0 and self.number1 != 0:
            raise ZeroDivisionError("denominator can't be 0")
        if type(self.number1) != int and type(self.number2) != int:
            raise NotImplementedError("the numerator and denominator must be int type")
        if self.number1 > 0 and self.number2 < 0 or self.number2 > 0 and self.number1 < 0:
            raise NotImplementedError("the numerator and denominator must be with the same module")

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise NotImplementedError('the numbers must be fractions')
        if self.number2 == other.number2:
            new_number1 = self.number1 + other.number1
            new_number2 = self.number2
            if new_number1 == 0:
                return Fraction(0, 0)
            if new_number1 %2 == 0 and new_number2 %2 == 0:
                new_number1 = new_number1 / 2
                new_number2 = new_number2 / 2
            if new_number2 % new_number1 == 0:
                new_number2 = new_number2 / new_number1
                new_number1 = new_number1 / new_number1
            return Fraction(int(new_number1), int(new_number2))
        elif self.number2 != other.number2:
            new_number1 = self.number1 * other.number2 + self.number2 * other.number1
            new_number2 = self.number2 * other.number2
            if new_number1 == 0:
                return Fraction(0, 0)
            if new_number1 % 2 == 0 and new_number2 % 2 == 0:
                new_number1 = new_number1 / 2
                new_number2 = new_number2 / 2
            if new_number2 % new_number1 == 0:
                new_number2 = new_number2 / new_number1
                new_number1 = new_number1 / new_number1
            return Fraction(int(new_number1), int(new_number2))

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise NotImplementedError('the numbers must be fractions')
        if self.number2 == other.number2:
            new_number1 = self.number1 - other.number1
            new_number2 = self.number2
            if new_number1 == 0:
                return Fraction(0, 0)
            if new_number1 % 2 == 0 and new_number2 % 2 == 0:
                new_number1 = new_number1 / 2
                new_number2 = new_number2 / 2
            if new_number2 % new_number1 == 0:
                new_number2 = new_number2 / new_number1
                new_number1 = new_number1 / new_number1
            return Fraction(int(new_number1), int(new_number2))
        elif self.number2 != other.number2:
            new_number1 = self.number1 * other.number2 - self.number2 * other.number1
            new_number2 = self.number2 * other.number2
            if new_number1 == 0:
                return Fraction(0, 0)
            if new_number1 % 2 == 0 and new_number2 % 2 == 0:
                new_number1 = new_number1 / 2
                new_number2 = new_number2 / 2
            if new_number2 % new_number1 == 0:
                new_number2 = new_number2 / new_number1
                new_number1 = new_number1 / new_number1
            return Fraction(int(new_number1), int(new_number2))

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise NotImplementedError('the numbers must be fractions')
        new_number1 = self.number1 * other.number1
        new_number2 = self.number2 * other.number2
        if new_number1 % 2 == 0 and new_number2 % 2 == 0:
            new_number1 = new_number1 / 2
            new_number2 = new_number2 / 2
        if new_number2 % new_number1 == 0:
            new_number2 = new_number2 / new_number1
            new_number1 = new_number1 / new_number1
        return Fraction(int(new_number1), int(new_number2))

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise NotImplementedError('the numbers must be fractions')
        new_number1 = self.number1 * other.number2
        new_number2 = self.number2 * other.number1
        if new_number1 % 2 == 0 and new_number2 % 2 == 0:
            new_number1 = new_number1 / 2
            new_number2 = new_number2 / 2
        if new_number2 % new_number1 == 0:
            new_number2 = new_number2 / new_number1
            new_number1 = new_number1 / new_number1
        return Fraction(int(new_number1), int(new_number2))

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            raise NotImplementedError('the numbers must be fractions')
        return self.number1 == other.number1 and self.number2 == other.number2

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            raise NotImplementedError('the numbers must be fractions')
        if self.number2 == other.number2:
            return self.number1 < other.number1
        elif self.number2 != other.number2:
            self.number1 = self.number1 * other.number2 + self.number2 * other.number1
            other.number1 = self.number2 * other.number1
            return self.number1 < other.number1

    def __le__(self, other):
        if not isinstance(other, Fraction):
            raise NotImplementedError('the numbers must be fractions')
        if self.number2 == other.number2:
            return self.number1 <= other.number1
        elif self.number2 != other.number2:
            self.number1 = self.number1 * other.number2 + self.number2 * other.number1
            other.number1 = self.number2 * other.number1
            return self.number1 <= other.number1

    def __ne__(self, other):
        if not isinstance(other, Fraction):
            raise NotImplementedError('the numbers must be fractions')
        if self.number2 == other.number2:
            return self.number1 != other.number1
        elif self.number2 != other.number2:
            self.number1 = self.number1 * other.number2 + self.number2 * other.number1
            other.number1 = self.number2 * other.number1
            return self.number1 != other.number1

    def __gt__(self, other):
        if not isinstance(other, Fraction):
            raise NotImplementedError('the numbers must be fractions')
        if self.number2 == other.number2:
            return self.number1 > other.number1
        elif self.number2 != other.number2:
            self.number1 = self.number1 * other.number2 + self.number2 * other.number1
            other.number1 = self.number2 * other.number1
            return self.number1 > other.number1

    def __ge__(self, other):
        if not isinstance(other, Fraction):
            raise NotImplementedError('the numbers must be fractions')
        if self.number2 == other.number2:
            return self.number1 >= other.number1
        elif self.number2 != other.number2:
            self.number1 = self.number1 * other.number2 + self.number2 * other.number1
            other.number1 = self.number2 * other.number1
            return self.number1 >= other.number1

    def __str__(self):
        return f'{self.number1}, {self.number2}'

if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print(x + y == Fraction(3, 4))
    print(x - y == Fraction(1, 4))
    print(x * y == Fraction(1, 8))
    print(x / y == Fraction(2, 1))
    print(x < y)
    print(x <= y)
    print(x != y)
    print(x > y)
    print(x >= y)