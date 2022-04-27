from models.LinkedList import LinkedList
from models import Node

def main():

    lista_ligada = LinkedList()
    while True:
        try:
            comandos = input().split()
        except EOFError:
            return
        if comandos[0] == "RPI":
            lista_ligada.insert_at_start(comandos[1])
            lista_ligada.traverse_list()
        elif comandos[0] == "RPF":
            lista_ligada.insert_at_end(comandos[1])
            lista_ligada.traverse_list()
        elif comandos[0] == "RPDE":
            lista_ligada.insert_after_item(comandos[2], comandos[1])
            lista_ligada.traverse_list()
        elif comandos[0] == "RPAE":
            lista_ligada.insert_before_item(comandos[2], comandos[1])
            lista_ligada.traverse_list()
        elif comandos[0] == "RPII":
            lista_ligada.insert_at_index(int(comandos[2]), comandos[1])
            lista_ligada.traverse_list()
        elif comandos[0] == "VNE":
            resposta = lista_ligada.get_count()
            print(f"O número de elementos são {resposta}.")
        elif comandos[0] == "VP":
            if lista_ligada.search_item(comandos[1]) == True:
                print(f"O país {comandos[1]} encontra-se na lista.")
            else:
                print(f"O país {comandos[1]} não se encontra na lista.")
        elif comandos[0] == "EPE":
            resposta = lista_ligada.start_node.item
            lista_ligada.delete_at_start()
            print(f"O país {resposta} foi eliminado da lista.")
        elif comandos[0] == "EUE":
            elemento = lista_ligada.get_last_node()
            lista_ligada.delete_at_end()
            print(f"O país {elemento} foi eliminado da lista.")
        elif comandos[0] == "EP":
            if lista_ligada.search_item(comandos[1]) == True:
                lista_ligada.delete_element_by_value(comandos[1])
                print(f"O país {comandos[1]} foi eliminado da lista.")
            else:
                print(f"O país {comandos[1]} não se encontra na lista.")
            
        else:
            print("Operação inválida.")
            

    