#SISTEMA DE ARMAZENAMENTO DE NOMES DE PAÍSES

#PROGRAMA CONSISTE EM ARMAZENANR NOMES DE PAÍSES E MANIPULA-LOS CONFORME INSTRUÇºOES DO USÚARIO.

#DEVE SER INSERIDO NO TERMINAL OS SEGUINTES COMANDOS CONFORME AS DEFINIÇÕES:
#RPI - Registrar um novo pais no inicio da lista. PARÂMETROS A SEREM INSERIDOS NO TERMINAL: RPI país_novo
#RPF - Registrar um novo país no final da lista. PARÂMETROS A SEREM INSERIDOS NO TERMINAL: RPF país_novo
#RPDE - Registrar um novo país depois de outro elemesnto já registrado. PARÂMETROS A SEREM INSERIDOS NO TERMINAL: RPDE país_novo país_registado
#RPAE - Registrar um novo país antes de outro elemesnto já registrado.  PARÂMETROS A SEREM INSERIDOS NO TERMINAL: RPAE país_novo país_registado
#RPII - Registrar país num determinado indice.  PARÂMETROS A SEREM INSERIDOS NO TERMINAL: RPII país_novo indice
#VNE - Verificar número de países na lista.  PARÂMETROS A SEREM INSERIDOS NO TERMINAL: VNE
#VP - Verificar se um determinado país está na lista.  PARÂMETROS A SEREM INSERIDOS NO TERMINAL: VP nome_do_país
#EPE - Eliminar o primeiro país da lista.  PARÂMETROS A SEREM INSERIDOS NO TERMINAL: EPE
#EUE - Eliminar o úkltimo país da lista.  PARÂMETROS A SEREM INSERIDOS NO TERMINAL: EUE
#EP - Eliminar um determinado país da lista.  PARÂMETROS A SEREM INSERIDOS NO TERMINAL: EP nome_do_país

#AUTOR: FELIPE GOES MAT.30009484 ESTUDANTE DE ENGENHARIA DE INFORMÁTICA



import encodings
import sys
from views import view
sys.stdout.reconfigure(encoding="utf-8")

if __name__ == "__main__":
    view.main()