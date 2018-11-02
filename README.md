
<img src="imagens/LogoIFSCCampusSJ.png" alt="IFSC" width="230" height="150"/>

## Engenharia de Telecomunicações
### Projeto Integrador 2018-2

**Grupo 1:**   
Allex Magno Andrade \
Douglas Amorim dos Santos \
Filipe Kuhnen

Projeto desenvolvido pelos alunos do curso de Engenharia de Telecomunicações
para validação teórica e prática da diciplina Projeto Integrador II.

O projeto consistem em desenvolver um robô seguidor de linhas para realizar
caças em um tabuleiro 6X6; Um Sistema surpevisor que irá comunicar com este robô e
um Sistema Autidor que irá ditar as regras do jogo.

Este repositório está organizado da seguinte maneira: 
* __Diagramas:__ Contém os arquivos de projeto (astah) dos diagramas de casos de uso, classes e sequência;\
* __Imagens:__ Contém as imagens exportadas dos diagramas; 
* __sistema_robo:__ Implementação do sistema robô. Progresso [=========>____] 
* __sistema_supervisor:__ Implementação do sistema supervisor. Progresso [=>____________] 
* __Sistema_auditor:__ Implementação do sistema Auditor. TODO 

Os robô utilizados no projeto são: [LEGOs Mindstroms
EV3](https://www.lego.com/en-us/mindstorms/products/mindstorms-ev3-31313)

*Sumario Portas Utilizadas:*

**__Comunicação SS -> SR:__**
* __62255 :__ Porta Usada para o Robo divulgar seu IP por BroadCast
* __65256 :__ Porta Usada para o SS divulgar seu IP por BroadCast
* __61030 :__ Porta Usada pelo SS para mandar instrução ao robo (modo autonomo, modo manual etc)
* __61031 :__ Porta Usada para a comunicação no modo Manual (utilizando Pyro4)
* __63030 :__ Porta Usada para a comunicação no modo Manual



