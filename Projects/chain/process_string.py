from abc import ABCMeta, abstractmethod


class StringValidator:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.next = None

    def chain(self, next):
        self.next = next
        return next

    def process(self, string):
        validated_str = self.validate(string)
        if self.next is not None:
            self.next.process(validated_str)

    def validate(self, string):
        raise NotImplementedError("You should implement this method.")


class LowerValidator(StringValidator):
    def validate(self, string):
        if not string.islower():
            raise Exception("String should be lowercase.")
        return string


class EmptyValidator(StringValidator):
    def validate(self, string):
        if not string:
            raise Exception("String should not be empty.")
        return string


class LengthValidator(StringValidator):
    def validate(self, string):
        if len(string) >= 50:
            raise Exception("String should be less than 100 characters.")
        return string


def validate_string(string: str) -> str:
    validator = LowerValidator()

    validator.chain(
        EmptyValidator()).chain(
        LengthValidator()
    )

    validator.process(string)


validate_string('hello')
