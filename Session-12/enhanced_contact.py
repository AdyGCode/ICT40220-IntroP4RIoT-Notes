"""
Enhanced Contact Class

Used for demonstrating inheritance

------------------------------------------------------------------------------
Project:   ICT40220-IntroP4RIoT-Notes
Folder:    Session-12
Filename:  contact.py
Author:    Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
Version:   0.0
------------------------------------------------------------------------------
"""

from contact import Contact


class EnhancedContact(Contact):

    def __init__(self, name, e_mail, city):
        # Call the Super Class (Contact) constructor to
        # save the name and email
        super().__init__(name, e_mail)
        # Add the city details
        self.city = city


if __name__ == '__main__':
    print("This is the Enhanced Contact class, and does not execute")
