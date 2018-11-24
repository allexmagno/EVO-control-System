from threading import Thread
from mensagens import *
from sacomTX import *
from sacomRX import *
from copy import deepcopy
import compartilhados
from distributor import *
from com import *


class Switch(Thread):
    compartilhados.init()

    def __init__(self, dist):
        Thread.__init__(self)


        self.distributor = dist

        self.srCOM = Com(65000)
        self.srCOM.rx()

        self.tx = SAcomTX('localhost')
        self.tx.start()

        self.rx = SAcomRX('localhost')
        self.rx.start()


    def _envia_msg_sa(self, msg):
         with compartilhados.sa_lock:
            compartilhados.sa_msg = msg
            compartilhados.sa_event.set()

    def _envia_msg_sr(self, msg):
        with compartilhados.lock:
            compartilhados.msg = msg
            compartilhados.sr_event.set()

    def _avisa_autonomo(self, msg):
        with compartilhados.autonomo_lock:
            compartilhados.autonomo_msg = msg
            compartilhados.autonomo_event.set()
        print("msg do avisa:")

    def _avisa_main(self, msg):
        with compartilhados.main_lock:
            compartilhados.main_msg = msg
            compartilhados.main_event.set()

    def run(self):

        while True:
            compartilhados.sw_event.wait()

            with compartilhados.sw_lock:
                msg = deepcopy(compartilhados.sw_msg)
                print(msg)

                if msg['_dir'] == 'sa':
                    # Mensagens Vinda do SA
                    if 'cmd' not in msg:
                        switch_event.clear()
                        continue

                    cmd = msg['cmd']
                    robo = self.distributor.getNome()
                    x, y = self.distributor.getCoord()
                    if cmd == SA_to_SS.ValidacaoCaca:
                        if msg['ack'] == 1:
                            self.distributor.setValidacao(True)
                        else:
                            self.distributor.setValidacao(False)

                        msg = {'cmd': SS_to_SR.ValidaCaca}
                        self._envia_msg_sr(msg)

                    elif cmd == SA_to_SS.AtualizaMapa:
                        pass

                    elif cmd == SA_to_SS.CadastraRobo:
                        pass

                    elif cmd == SA_to_SS.Continua:
                        pass

                    elif cmd == SA_to_SS.Pausa:
                        pass

                    elif cmd == SA_to_SS.FimJogo:
                        pass

                    elif cmd == SA_to_SS.NovoJogo:
                        pass


                elif 'cmd' in msg and msg['cmd'] != 'auto' :
                    print("switch msg SR")
                    # Mensagens vindas do robo
                    msg = msg['cmd'].split("|")
                    cmd = msg[0]
                    robo = self.distributor.getNome()
                    print(msg)
                    x = int(msg[1][0])
                    y = int(msg[1][1])
                    if cmd == "destino":
                        msg = {'_dir':'sa', '_robo': robo, 'cmd': SS_to_SA.MovendoPara, 'x': x, 'y': y}
                        self.distributor.setCoord(x, y)
                        self._avisa_autonomo({'cmd':SS_to_SS.MovendoPara})
                        self._envia_msg_sa(msg)


                    elif cmd == "validar":
                        msg = {'robo': robo, 'cmd': SS_to_SA.ValidaCaca, 'x': x, 'y': y}

                        self._avisa_autonomo(msg)
                        self._envia_msg_sa(msg)

                    elif cmd == "posAtual":
                        msg = {'robo': robo, 'cmd': SS_to_SA.PosicaoAtual, 'x': x, 'y': y}
                        self._envia_msg_sa(msg)
                        self._avisa_autonomo(msg)

                    else:
                        return

                else:
                    msg = {'modo':'autonomo'}
                    self._avisa_main(msg)



                compartilhados.sw_event.clear()
