"""
Contact Class

Used for demonstrating inheritance

------------------------------------------------------------------------------
Project:   ICT40220-IntroP4RIoT-Notes
Folder:    Session-12
Filename:  contact.py
Author:    Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
Version:   0.0
------------------------------------------------------------------------------
"""


class Contact:

    def __init__(self, name, e_mail):
        # Store the name and email for the Contact
        self.name = name
        self.email = e_mail

    def __str__(self):
        return f"{self.name} <{self.email}>"


if __name__ == '__main__':
    print("This is the Contact class, and does not execute")
