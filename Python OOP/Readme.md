# Object-Oriented Programming (OOP) in Python

> TOPICS: `class`, `object`, `instance attributes`, `class attributes`, `inheritance`, `encapsulation`, `polymorphism`

- `Classes` define functions called methods, 
which identify the behaviors and actions 
that an object created from the class 
can perform with its data.

- `Instance` is an object that is built 
from a class and contains real data.
Instance object consists of attributes and methods.

- Attributes created in .__init__() are called `instance attributes`,
which are spesific only for an instance.

- `Class attributes` are attributes that have the same value for all class instances. 
You can define a class attribute by assigning a value to a variable name outside of .__init__().

- **Class**, which is a sort of blueprint for an object
- **Instantiate** an object from a class
- Use **attributes** and **methods** to define the **properties** and **behaviors** of an object
- Use **inheritance** to create **child classes** from a **parent class**
- Reference a method on a parent class using `super()` e.g. `super().__init__()`
- Check if an object inherits from another class using `isinstance()`
- **Polymorphism** allows the same interface for different objects, so programmers can write efficient code.


## References
- https://realpython.com/python3-object-oriented-programming/
- https://www.programiz.com/python-programming/object-oriented-programming
- https://realpython.com/oop-in-python-vs-java/
