# models.py
# import datetime # imports entire module/package/library name
from dataclasses import (
    dataclass,
)  # import a specific class/function from a module/package/library


@dataclass
class Person:
    name: str
    age: int = 0  # Default value for age is set to 0

    def is_adult(self) -> bool:
        """Method to check if the person is an adult (18 years or older)."""
        return self.age >= 18


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """
        __str__ is used for informal string representation of the object, often used for end-user display.

        String Interpolation:
        self.name + " is " + str(self.age) + " years old."
        f"{self.name} is {self.age} years old."
        """
        return (
            f"{self.name} is {self.age} years old."  # String Interpolation / f-strings
        )

    def __repr__(self):
        """
        __repr__ is used for the official string representation of an object,
        often used for debugging and development.
        """
        return f"Student(name={self.name!r}, age={self.age!r})"

    def __eq__(self, value: object) -> bool:
        """__eq__ is used to compare two objects for equality."""
        if not isinstance(value, Student):
            return False
        return self.name == value.name and self.age == value.age

    def is_adult(self):
        """
        Method to check if the student is an adult (18 years or older).
        """
        return self.age >= 18


if __name__ == "__main__":
    student1 = Student("Alice", 20)
    student2 = Student("Bob", 16)
    print(student1)  # Output: Alice is 20 years old.
    print(student2)  # Output: Bob is 16 years old.
    print("Student 1 is an adult:", student1.is_adult())  # Output: True
    print("Student 2 is an adult:", student2.is_adult())  # Output: False
    # Testing equality:
    student3 = Student("Alice", 20)
    print("Student 1 is equal to Student 3:", student1 == student3)  # Output: True

    person1 = Person("Charlie", 25)
    person2 = Person("Diana", 17)
    person3 = Person("Charlie", 25)
    print(person1)
    print(person1 == person3)  # Output: True
    print(person1.is_adult())  # Output: True
