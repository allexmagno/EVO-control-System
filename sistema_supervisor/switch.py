from threading import Thread, Lock, Event
from mensagens import *
from sacomTX import *
from sacomRX import *
from copy import deepcopy
import compartilhados
from distributor import *


class Switch(Thread):
    def __init__(self, hostSA, dist):
        super(Switch, self).__init__()

        compartilhados.init()
        self.distributor = dist

        self.tx = SAcomTX(hostSA)
        self.tx.start()

        self.rx = SAcomRX(hostSA)
        self.rx.start()

    def _envia_msg_sa(self, msg):
        with compartilhados.sa_lock:
            compartilhados.sa_msg = msg
            compartilhados.sa_event.set()

    def _envia_msg_sr(self, msg):
        with compartilhados.sr_lock:
            compartilhados.sr_msg = msg
            compartilhados.sr_event.set()

    def switch(self):
        def switch_rede():
            while True:

                compartilhados.switch_event.wait()

                with compartilhados.switch_lock:
                    msg = deepcopy(compartilhados.switch_msg)

                    if 'cmd' not in msg:
                        switch_event.clear()
                        continue

                    cmd = msg['cmd']
                    robo = self.distributor.getNome()
                    x, y = self.distributor.getCoord()
                    if '_dir' in msg and msg['_dir'] == 'sr' and cmd == -1:
                        break

                    # Mensagens vindas do SR
                    if '_dir' in msg and msg['_dir'] == 'sr':
                        print ("Recebendo mensagem do SR")

                        if cmd == SR_to_SS.MovendoPara:
                            msg = {'robo':robo, 'cmd':SS_to_SA.MovendoPara, 'x':x, 'y':y}
                            self._envia_msg_ss(msg)

                        elif cmd == SR_to_SS.PosicaoAtual:
                            msg = {'robo': robo, 'cmd': SS_to_SA.PosicaoAtual, 'x': x, 'y': y}
                            self._envia_msg_ss(msg)

                        elif cmd == SR_to_SS.ValidaCaca:
                            msg = {'robo': robo, 'cmd': SS_to_SA.ValidaCaca, 'x': x, 'y': y}
                            self._envia_msg_ss(msg)

                        elif cmd == SR_to_SS.ObstaculoEncontrado:
                            msg = {'robo': robo, 'cmd': SS_to_SA.ObstaculoEncontrado, 'x': x, 'y': y}
                            self._envia_msg_ss(msg)

                        else:
                            pass

                    # Mensagens vindas do SR
                    elif '_dir' in msg and msg['_dir'] == 'sa':
                        print("Recebendo mensagem do SA")

                        if cmd == SA_to_SS.ValidacaoCaca:

                            if msg['ack'] == 1:
                                self.distributor.setValidacao(True)
                            else:
                                self.distributor.setValidacao(False)

                            msg = {'cmd': SS_to_SR.ValidaCaca}
                            self._envia_msg_sr(msg)

                        elif cmg == SA_to_SS.AtualizaMapa:
                            pass

                        elif cmg == SA_to_SS.CadastraRobo:
                            pass

                        elif cmg == SA_to_SS.Continua:
                            pass

                        elif cmg == SA_to_SS.Pausa:
                            pass

                        elif cmg == SA_to_SS.FimJogo:
                            pass

                        elif cmg == SA_to_SS.NovoJogo:
                            pass

                        compartilhados.switch_event.clear()


        thread = Thread(target=switch_rede)
        thread.start()
        return

if __name__ == '__main__':
    print("Inicializando ...")
    distributor = Distributor("equipe1", 0, 0)
    switch = Switch('localhost',distributor)
    switch.switch()