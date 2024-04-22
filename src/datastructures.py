
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "id": 1,
                "name": "John Jackson",
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": 2,
                "name": "Jane Jackson",
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": 3,
                "name": "Jimmy Jackson",
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)
    


    def add_member(self, member):
        # fill this method and update the return
        if not member.get("id"):        # condicional, si member no tiene .get("id") con el .get() y no con [] para que no arroje error en caso de no cumplirse
            member["id"]= self._generateId()        # en caso de que no lo tenga, el condicional pasa a crearle un id con la función definida arriba
        self._members.append(member)        # se le añade el valor de member a member, creando así un nuevo miembro

        print("añadir miembro", member)



    def delete_member(self, id):
        # fill this method and update the return
        print("deleted", id)  
        for member in self._members:        # se realiza un bucle for in porque existe la posibilidad de que se esté intentando borrar un id no existente, por lo tanto
            if member["id"] == id:        # si el member["id"] (se debe señalar entre corchetes y a manera de string) es == igual a ID
                self._members.remove(member)        # se pone como target el lugar donde se encuentra contenido aquello que se quiere borrar y se le agrega .remove( con aquello que vamos a borrar )
                return True         # si el miembro existe retorna True que terminará generando el status 200
        return False        # de lo contrario para hacer el manejo de errores es necesario que se retorne False el cual resultará generando el status 400
    


    def update_member(self, id, member):
        print(id)
        for family_member in self._members:
            if family_member["id"] == id:
                self._members.remove(family_member)
                member["id"] = id
                self._members.append(member)
                return True
        return False
                
        

    def get_member(self, id):
        # fill this method and update the return
        for one_member in self._members:
            if one_member["id"] == id:
                return one_member
        return False
        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members



