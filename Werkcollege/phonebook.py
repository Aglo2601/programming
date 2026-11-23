class Phonebook:

    def __init__(
        self,
        contact_list: list[tuple[str, str]] | None = None,
    ) -> None:
        """
        >>> Phonebook()._contacts
        {}
        >>> Phonebook([("Ada", "123")])._contacts
        {'Ada': '123'}
        >>> Phonebook([]).count_contacts()
        0
        """
        self._contacts: dict[str, str] = dict(contact_list or [])

    def add_contact(self, name: str, number: str) -> None:
        """
        >>> pb = Phonebook(); pb.add_contact("Ada", "123"); 
        >>> pb.list_contacts()
        ['Ada']
        >>> pb = Phonebook(); pb.add_contact("Lin", "456"); 
        >>> pb.get_number("Lin")
        '456'
        >>> pb = Phonebook([("Ada", "123")]); pb.add_contact("Ada", "789")
        Traceback (most recent call last):
        ...
        KeyError: 'duplicate key'
        """
        if name in self._contacts:
            raise KeyError("duplicate key")
        self._contacts[name] = number

    def get_number(self, name: str) -> str | None:
        """
        >>> Phonebook([("Ada", "123")]).get_number("Ada")
        '123'
        >>> Phonebook().get_number("Ada") is None
        True
        >>> Phonebook([("Lin", "456")]).get_number("Lin")
        '456'
        """
        return self._contacts.get(name)

    def remove_contact(self, name: str) -> None:
        """
        >>> pb = Phonebook([("Ada", "123"), ("Lin", "456")]); 
        >>> pb.remove_contact("Ada"); pb.list_contacts()
        ['Lin']
        >>> pb = Phonebook([("Ada", "123")]); 
        >>> pb.remove_contact("Missing"); 
        >>> pb.count_contacts()
        1
        >>> pb = Phonebook([("Ada", "123"), ("Ada", "789")]); 
        >>> pb.remove_contact("Ada"); 
        >>> pb.list_contacts()
        []
        """
        self._contacts.pop(name, None)

    def update_number(self, name: str, new_number: str) -> None:
        """
        >>> pb = Phonebook([("Ada", "123")]); 
        >>> pb.update_number("Ada", "789"); 
        >>> pb.get_number("Ada")
        '789'
        >>> pb = Phonebook([("Ada", "123")]); 
        >>> pb.update_number("Missing", "789"); 
        >>> pb.get_number("Ada")
        '123'
        >>> pb = Phonebook([("Ada", "123"), ("Ada", "456")]); 
        >>> pb.update_number("Ada", "789"); pb.list_contacts()
        ['Ada']
        """
        if name in self._contacts:
            self._contacts[name] = new_number

    def list_contacts(self) -> list[str]:
        """
        >>> Phonebook().list_contacts()
        []
        >>> Phonebook([("Ada", "123")]).list_contacts()
        ['Ada']
        >>> Phonebook([("Ada", "123"), ("Lin", "456")]).list_contacts()
        ['Ada', 'Lin']
        """
        return sorted(self._contacts)




    def search_by_prefix(self, prefix: str) -> list[str]:
        """
        >>> Phonebook([("Ada", "123"), ("Lin", "456")]).search_by_prefix("A")
        ['Ada']
        >>> Phonebook([("Ada", "123"), ("Ann", "789")]).search_by_prefix("A")
        ['Ada', 'Ann']
        >>> Phonebook([("Ada", "123")]).search_by_prefix("Z")
        []
        """
        return sorted(
            contact_name
            for contact_name, contact_number in self._contacts.items()
            if contact_name.startswith(prefix)
        )

    def reverse_lookup(self, number: str) -> list[str]:
        """
        >>> Phonebook([("Ada", "123")]).reverse_lookup("123")
        ['Ada']
        >>> Phonebook([("Ada", "123"), ("Lin", "123")]).reverse_lookup("123")
        ['Ada', 'Lin']
        >>> Phonebook([("Ada", "123")]).reverse_lookup("999")
        []
        """
        return sorted(
            contact_name
            for contact_name, contact_number in self._contacts.items()
            if contact_number == number
        )

    def count_contacts(self) -> int:
        """
        >>> Phonebook().count_contacts()
        0
        >>> Phonebook([("Ada", "123")]).count_contacts()
        1
        >>> Phonebook([("Ada", "123"), ("Lin", "456")]).count_contacts()
        2
        """
        return len(self._contacts)

    def to_dict(self) -> dict[str, str]:
        """
        >>> Phonebook().to_dict()
        {}
        >>> Phonebook([("Ada", "123")]).to_dict()
        {'Ada': '123'}
        >>> Phonebook([("Ada", "123"), ("Lin", "456")]).to_dict()
        {'Ada': '123', 'Lin': '456'}
        """
        return {
            contact_name: contact_number
            for contact_name, contact_number in self._contacts.items()
        }

    def merge(self, other_Phonebook: 'Phonebook') -> 'Phonebook':
        """
        >>> Phonebook().merge(Phonebook()).list_contacts()
        []
        >>> Phonebook([("Ada", "123")]).merge(Phonebook()).list_contacts()
        ['Ada']
        >>> pb1 = Phonebook([("Ada", "123")])
        >>> pb2 = Phonebook([("Lin", "456")])
        >>> pb1.merge(pb2).list_contacts()
        ['Ada', 'Lin']
        """
        merged_contacts = self._contacts | other_Phonebook._contacts
        merged_Phonebook = Phonebook(list(merged_contacts.items()))

        return merged_Phonebook
    