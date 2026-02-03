#!/usr/bin/env python3
"""
Module defining an abstract Animal class and its subclasses Dog and Cat.
This module demonstrates the use of abstract base classes (ABC) in Python.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing a generic animal.

    This class defines a blueprint for all animals.
    Any subclass must implement the sound method.
    """

    @abstractmethod
    def sound(self):
        """
        Produce the sound of the animal.

        This method must be implemented by all subclasses.

        Returns:
            str: The sound made by the animal.
        """
        pass


class Dog(Animal):
    """
    Class representing a Dog, which is a subclass of Animal.
    """

    def sound(self):
        """
        Return the sound made by the dog.

        Returns:
            str: "Bark"
        """
        return "Bark"


class Cat(Animal):
    """
    Class representing a Cat, which is a subclass of Animal.
    """

    def sound(self):
        """
        Return the sound made by the cat.

        Returns:
            str: "Meow"
        """
        return "Meow"
