class phonebook:

    def __init__(self, contact_list=None) -> None:
        """
        >>> phonebook().contact_list
        []
        >>> phonebook([("Ada", "123")]).contact_list
        [('Ada', '123')]
        >>> phonebook([]).count_contacts()
        0
        """
        self.contact_list = contact_list if contact_list is not None else []

    def add_contact(self, name, number) -> None:
        """
        >>> pb = phonebook(); pb.add_contact("Ada", "123"); pb.list_contacts()
        [('Ada', '123')]
        >>> pb = phonebook(); pb.add_contact("Lin", "456"); pb.get_number("Lin")
        '456'
        >>> pb = phonebook([("Ada", "123")]); pb.add_contact("Ada", "789")
        Traceback (most recent call last):
        ...
        KeyError: 'duplicate key'
        """
        if any(contact_name == name for contact_name, _ in self.contact_list):
            raise KeyError("duplicate key")
        self.contact_list.append((name, number))

    def get_number(self, name) -> str | None:
        """
        >>> phonebook([("Ada", "123")]).get_number("Ada")
        '123'
        >>> phonebook().get_number("Ada") is None
        True
        >>> phonebook([("Lin", "456")]).get_number("Lin")
        '456'
        """
        for contact_name, contact_number in self.contact_list:
            if contact_name == name:
                return contact_number
        return None

    def remove_contact(self, name) -> None:
        """
        >>> pb = phonebook([("Ada", "123"), ("Lin", "456")]); pb.remove_contact("Ada"); pb.list_contacts()
        [('Lin', '456')]
        >>> pb = phonebook([("Ada", "123")]); pb.remove_contact("Missing"); pb.count_contacts()
        1
        >>> pb = phonebook([("Ada", "123"), ("Ada", "789")]); pb.remove_contact("Ada"); pb.list_contacts()
        []
        """
        self.contact_list = [
            (contact_name, contact_number) 
            for contact_name, contact_number in self.contact_list if contact_name != name
            ]

    def update_number(self, name, new_number) -> None:
        """
        >>> pb = phonebook([("Ada", "123")]); pb.update_number("Ada", "789"); pb.get_number("Ada")
        '789'
        >>> pb = phonebook([("Ada", "123")]); pb.update_number("Missing", "789"); pb.get_number("Ada")
        '123'
        >>> pb = phonebook([("Ada", "123"), ("Ada", "456")]); pb.update_number("Ada", "789"); pb.list_contacts()
        [('Ada', '789'), ('Ada', '789')]
        """
        self.contact_list = [
            (contact_name, new_number) if contact_name == name else (contact_name, contact_number)
            for contact_name, contact_number in self.contact_list
        ]

    def list_contacts(self) -> list[tuple[str, str]]:
        """
        >>> phonebook().list_contacts()
        []
        >>> phonebook([("Ada", "123")]).list_contacts()
        [('Ada', '123')]
        >>> phonebook([("Ada", "123"), ("Lin", "456")]).list_contacts()
        [('Ada', '123'), ('Lin', '456')]
        """
        return self.contact_list

    def search_by_prefix(self, prefix) -> list[tuple[str, str]]:
        """
        >>> phonebook([("Ada", "123"), ("Lin", "456")]).search_by_prefix("A")
        [('Ada', '123')]
        >>> phonebook([("Ada", "123"), ("Ann", "789")]).search_by_prefix("A")
        [('Ada', '123'), ('Ann', '789')]
        >>> phonebook([("Ada", "123")]).search_by_prefix("Z")
        []
        """
        return [
            (contact_name, contact_number) 
            for contact_name, contact_number in self.contact_list if contact_name.startswith(prefix)
            ]
    
    def reverse_lookup(self, number) -> list[str]:
        """
        >>> phonebook([("Ada", "123")]).reverse_lookup("123")
        ['Ada']
        >>> phonebook([("Ada", "123"), ("Lin", "123")]).reverse_lookup("123")
        ['Ada', 'Lin']
        >>> phonebook([("Ada", "123")]).reverse_lookup("999")
        []
        """
        return [contact_name for contact_name, contact_number in self.contact_list if contact_number == number]

    def count_contacts(self) -> int:
        """
        >>> phonebook().count_contacts()
        0
        >>> phonebook([("Ada", "123")]).count_contacts()
        1
        >>> phonebook([("Ada", "123"), ("Lin", "456")]).count_contacts()
        2
        """
        return len(self.contact_list)  

    def to_dict(self) -> dict[str, str]:
        """
        >>> phonebook().to_dict()
        {}
        >>> phonebook([("Ada", "123")]).to_dict()
        {'Ada': '123'}
        >>> phonebook([("Ada", "123"), ("Lin", "456")]).to_dict()
        {'Ada': '123', 'Lin': '456'}
        """
        return {contact_name: contact_number for contact_name, contact_number in self.contact_list}

    def merge(self, other_phonebook) -> 'phonebook':
        """
        >>> phonebook().merge(phonebook()).list_contacts()
        []
        >>> phonebook([("Ada", "123")]).merge(phonebook()).list_contacts()
        [('Ada', '123')]
        >>> phonebook([("Ada", "123")]).merge(phonebook([("Lin", "456")])).list_contacts()
        [('Ada', '123'), ('Lin', '456')]
        """
        merged_contacts = self.contact_list + other_phonebook.contact_list
        merged_phonebook = phonebook(merged_contacts)

        return merged_phonebook
    