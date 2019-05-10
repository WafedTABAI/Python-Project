from Donnees.mainManag import mainManag
from Donnees.mainServer import mainServer

import threading

#declaration of the mutex to synchronize the acces to the database
mutexComptes = threading.Lock()
mutexTransactions = threading.Lock()
mutexFactures = threading.Lock()


thread_1 = mainManag(mutexComptes,mutexTransactions,mutexFactures)
thread_2 = mainServer(mutexComptes,mutexTransactions,mutexFactures)


thread_1.start()
thread_2.start()