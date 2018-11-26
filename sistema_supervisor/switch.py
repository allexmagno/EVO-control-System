from threading import Thread
from mensagens import *
from sacomTX import *
from sacomRX import *
from copy import deepcopy
import compartilhados
from distributor import *
from com import *
import time


class Switch(Thread):
    compartilhados.init()

    def __init__(self, dist):
        Thread.__init__(self)


        self.distributor = dist

        self.srCOM = Com(65000)
        mac = self.srCOM.descoberta()
        self.distributor.setMac(mac)
        self.srCOM.rx()

        self.tx = SAcomTX('localhost')
        self.tx.start()

        self.rx = SAcomRX('localhost', self.distributor.getNome())
        self.rx.start()

    def _envia_msg_sa(self, msg):
         with compartilhados.sa_lock:
            compartilhados.sa_msg = msg
            compartilhados.sa_event.set()

    def _envia_msg_sr(self, msg):
        #with compartilhados.lock:
        #    compartilhados.msg = msg
        #    compartilhados.sr_event.set()
        self.srCOM.enviar(self.srCOM.getRobo(), msg)

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
        #lista = 'lista|12/22/23'
        while True:
            compartilhados.sw_event.wait()

            with compartilhados.sw_lock:
                msg = deepcopy(compartilhados.sw_msg)
                print(msg)

                if msg['_dir'] == 'sa':
                    # Mensagens Vinda do SA
                    if 'cmd' not in msg:
                        compartilhados.sw_event.clear()
                        continue

                    cmd = msg['cmd']
                    if cmd == SA_to_SS.ValidacaoCaca:
                        if msg['ack'] == 1:
                            self.distributor.setValidacao(True)
                            msg = {'cmd': SS_to_SS.ValidaCaca_resp, 'caca': 1}
                            self._avisa_main(msg)

                        else:
                            self.distributor.setValidacao(False)
                            msg = {'cmd': SS_to_SS.ValidaCaca_resp, 'caca': 0}
                            self._avisa_main(msg)

                        #msg = {'cmd': SS_to_SR.ValidaCaca}
                        #self._envia_msg_sr(msg)

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
                        if msg['modo_jogo'] == 'autonomo':
                            self._avisa_main({'modo': 'auto'})

                            coord = msg['x'] + msg['y']
                            self.srCOM.enviar(self.srCOM.getRobo(), coord)
                            self.srCOM.enviar(self.srCOM.getRobo(), 'auto')

                            ## TRATAR AS CAÇAS
                            self.srCOM.enviar(self.srCOM.getRobo(), msg['cacas'])


                        elif msg['modo_jogo'] == 'manual':
                            coord = msg['x'] + msg['y']
                            self.srCOM.enviar(self.srCOM.getRobo(), coord)
                            self.srCOM.enviar(self.srCOM.getRobo(), 'manual')


                elif msg['_dir'] == 'ss':
                    # Mensagens Vinda do Ss
                    if 'cmd' not in msg:
                        compartilhados.sw_event.clear()
                        continue

                    elif msg['cmd'] == SS_to_SS.ValidaCaca:
                        msg = {'_dir': 'ss', '_robo': self.distributor.getNome(),
                               'cmd': SS_to_SA.ValidaCaca, 'x': msg['x'], 'y': msg['y']}
                        self._envia_msg_sa(msg)




                elif msg['_dir'] == 'sr':
                    # Mensagens vindas do robo
                    msg = msg['cmd'].split("|")
                    cmd = msg[0]
                    robo = self.distributor.getNome()


                    if cmd == "destino":
                        x = int(msg[1][0])
                        y = int(msg[1][1])
                        msg = {'_dir':'sa', '_robo': robo, 'cmd': SS_to_SA.MovendoPara, 'x': x, 'y': y}
                        self.distributor.setCoord(x, y)
                        self._avisa_autonomo({'cmd':SS_to_SS.MovendoPara})
                        self._envia_msg_sa(msg)



                    elif cmd == "validar":
                        x = int(msg[1][0])
                        y = int(msg[1][1])
                        msg = {'robo': robo, 'cmd': SS_to_SA.ValidaCaca, 'x': x, 'y': y}

                        self._avisa_autonomo({'cmd':SS_to_SS.ValidaCaca})
                        self._envia_msg_sa(msg)

                        #print('SA VALIDANDO CAÇA')
                        #time.sleep(2)
                        #print('Caça validada')
                        #self.srCOM.enviar(self.srCOM.getRobo(), 'validada'+'|'+'22/23')

                    elif cmd == "posAtual":
                        x = int(msg[1][0])
                        y = int(msg[1][1])
                        msg = {'robo': robo, 'cmd': SS_to_SA.PosicaoAtual, 'x': x, 'y': y}
                        self._envia_msg_sa(msg)
                        self._avisa_autonomo(msg)
                        self.srCOM.enviar(self.srCOM.getRobo(), lista)

                    elif cmd == "mac":
                        print("Recebendo MAC:", msg[1])
                        self.distributor.setMac(msg[1])

                    elif cmd == "uri":
                        msg = {'modo':'manual', 'uri': msg[1]}
                        self._avisa_main(msg)

                    elif cmd == "manual":
                        self.srCOM.enviar(self.srCOM.getRobo(), '00')
                        self.srCOM.enviar(self.srCOM.getRobo(), 'manual')

                    else:
                        return

                else:

                    msg = {'modo': 'auto'}

                    self._avisa_main(msg)
                    self.srCOM.enviar(self.srCOM.getRobo(), '00')
                    self.srCOM.enviar(self.srCOM.getRobo(), msg['modo'])
                    self.srCOM.enviar(self.srCOM.getRobo(), lista)



                compartilhados.sw_event.clear()
