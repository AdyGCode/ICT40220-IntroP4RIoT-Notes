# Python Classes References / Tutorials

## Interface Classes in Python

Reference; Kant, S. (2023, April 10). Interfaces and Abstract Classes in Python: Understanding the Differences. Medium. https://medium.com/@shashikantrbl123/interfaces-and-abstract-classes-in-python-understanding-the-differences-3e5889a0746a

Interfaces and abstract classes are two important concepts in object-oriented programming. They allow us to write clean, maintainable, and flexible code. In this blog post, we’ll explore the similarities and differences between interfaces and abstract classes in Python, and learn when to use each approach.


### What is an interface?
An interface defines a contract between a class and its users. It specifies a set of methods that a class must implement in order to be considered compatible with the interface. In Python, interfaces can be implemented using abstract base classes (ABCs).

For example, suppose we have a Shape interface that specifies a single method, area(). We can define the Shape interface in Python using the abc module as follows:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

```

Now, any class that implements the Shape interface must provide an implementation of the area() method.

### Implementing interfaces in Python

To implement an interface in Python, we create a class that inherits from the interface’s abstract base class. We then provide implementations for all the required methods.

For example, suppose we want to implement the Shape interface for a Rectangle class. We can do so as follows:

```python

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
        # This has to be implemented as the Interface Class (Shape) requires it.
        # try commenting out these two lines and running the code in `rectangle.py`
    def area(self):
        return self.width * self.height
```

Notice that we didn’t explicitly inherit from the Shape interface. Instead, we provided an implementation of the area() method, which is all that’s required to be compatible with the Shape interface.

### What is an abstract class?

An abstract class is a class that cannot be instantiated directly. Instead, it’s intended to be subclassed by other classes that provide concrete implementations of its abstract methods. Abstract classes are useful for defining a common interface for a group of related classes.

For example, suppose we have a Vehicle abstract class that defines a common interface for all types of vehicles. We can define the Vehicle abstract class in Python using the abc module as follows:
```python

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass
    
    @abstractmethod
    def accelerate(self):
        pass
    
    @abstractmethod
    def brake(self):
        pass
```

Now, any class that inherits from the Vehicle abstract class must provide concrete implementations of the start_engine(), stop_engine(), accelerate(), and brake() methods.

### Implementing abstract classes in Python

To implement an abstract class in Python, we create a subclass that inherits from the abstract class and provides concrete implementations of its abstract methods.

For example, suppose we want to implement the Vehicle abstract class for a Car class. We can do so as follows:
```python

class Car(Vehicle):
    def start_engine(self):
        print("Starting car engine...")
    
    def stop_engine(self):
        print("Stopping car engine...")
    
    def accelerate(self):
        print("Accelerating car...")
    
    def brake(self):
        print("Applying car brakes...")
```

Notice that we provided concrete implementations of all the abstract methods defined in the Vehicle abstract class.

### Differences between interfaces and abstract classes

Interfaces and abstract classes have some similarities, but there are also some key differences. Interfaces focus on defining a contract between a class and its users, while abstract classes focus on defining a common interface for a group of related classes.

In general, interfaces cannot define any implementation, while abstract classes can define both abstract methods and concrete methods. This means that interfaces are more restrictive than abstract classes.

Another difference between interfaces and abstract classes is that a class can implement multiple interfaces, but it can only inherit from a single abstract class. This makes interfaces more flexible than abstract classes in terms of class design.

In addition, interfaces can be used for duck typing, which means that a class is considered compatible with an interface as long as it provides the required methods, regardless of its inheritance hierarchy. Abstract classes, on the other hand, require explicit inheritance and implementation.

### When to use interfaces and abstract classes

Interfaces are useful when you want to define a contract between a class and its users. They’re particularly useful for defining APIs and ensuring that classes are compatible with each other.

Abstract classes, on the other hand, are useful when you want to define a common interface for a group of related classes. They’re particularly useful for implementing a template method pattern, where the abstract class defines a skeleton for an algorithm and the concrete subclasses provide specific implementations for each step.



### Written Tutorials

- Real Python. (2024). Python Classes: The Power of Object-Oriented Programming – Real Python. Realpython.com. https://realpython.com/python-classes/
- Murphy, W. (2020, February 10). Implementing an Interface in Python. Realpython.com; Real Python. https://realpython.com/python-interface/
- Ramos, L. P. (2025, January 19). Python Class Constructors: Control Your Object Instantiation. Realpython.com; Real Python. https://realpython.com/python-class-constructor/
- Ramos, L. P. (2025, January 12). Variables in Python: Usage and Best Practices. Realpython.com; Real Python. https://realpython.com/python-variables/
- Rodriguez, I. (2025, January 11). Inheritance and Composition: A Python OOP Guide. Realpython.com; Real Python. https://realpython.com/inheritance-composition-python/
- Ramos, L. P. (2024, February 26). Duck Typing in Python: Writing Flexible and Decoupled Code. Realpython.com; Real Python. https://realpython.com/duck-typing-python/
- Ramos, L. P. (2025, January 20). Getters and Setters: Manage Attributes in Python. Realpython.com; Real Python. https://realpython.com/python-getter-setter/
    
### Video Tutorials
- Bro Code. (2024, July 7). Python Object-Oriented Programming (Full Course). Youtube.com. https://www.youtube.com/watch?v=IbMDCwVm63M
- Idently. (2024, August 30). Learn Python OOP in 20 Minutes. Youtube.com. https://www.youtube.com/watch?v=rLyYb7BFgQI
- Python Simplified. (2021, July 16). Python Classes and Objects - OOP for Beginners. Youtube.com. https://www.youtube.com/watch?v=f0TrMH9s-VE
- Python Simplified. (2022, March 22). OOP Class Inheritance and Private Class Members - Python for Beginners. Youtube.com. https://www.youtube.com/watch?v=6c6NYPjO_rI&list=PLqXS1b2lRpYRCbHe3sG5viisehpADOWUv&index=3
- Python Simplified. (2022, November 27). If __name__ == “__main__” for Python Developers. Youtube.com. https://www.youtube.com/watch?v=NB5LGzmSiCs

#### More advanced topics (for second semester)
- Python Simplified. (2022, November 8). Python TDD Workflow - Unit Testing Code Example for Beginners. Youtube.com. https://www.youtube.com/watch?v=ibVSPVz2LAA&list=PLqXS1b2lRpYRCbHe3sG5viisehpADOWUv&index=5



# Mermaid Flowcharts

```mermaid
flowchart TD
  start_code([start])
  end_code([end])
  A[Get Name]
  B[Get Year]
  C[[Calculate Age]]
  D[/Display Age/]
  E{age > 18}
  F[/display you can vote/]
  G[/display we value your opinion, but no voting for you/]
    
  start_code --> A
  A --> B
  B --> C
  C --> D
  D --> E
  E --> |yes| F
  E --> |no| G

  F --> end_code
  G --> end_code

  
```