"""
Demonstration of Inheritance

Uses the Contact and Enhanced Contact classes to
demonstrate the OO Principle of Inheritance

------------------------------------------------------------------------------
Project:   ICT40220-IntroP4RIoT-Notes
Folder:    Session-12
Filename:  inheritance-demo-1.py
Author:    Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
Version:   0.0
------------------------------------------------------------------------------
"""

from contact import Contact
from enhanced_contact import EnhancedContact


def demo():
    contact_one = Contact("Jacques d'Carre",
                          "jacques@example.com")
    contact_two = EnhancedContact("Eileen Dover",
                                  "eileen@example.com",
                                  "Étretat")

    print(f"Contact 1: {contact_one}")
    print(f"Contact 2: {contact_two}")


if __name__ == '__main__':
    demo()
