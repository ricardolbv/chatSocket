## SISTEMAS DISTRIBUÍDOS PROJETO: CHAT

#### 1. OBJETIVO

##### Implementar um serviço de chat usando sockets. Neste serviço,clientes cadastram os usernames dos usuários junto ao servidor, que divulga os usernames dos usuários logados no sistema.

##### A partir disso, os clientes podem trocar mensagens.

#### 2. DESCRIÇÃO GERAL

##### O sistema deverá ser composto por um servidor e clientes.

##### O servidor ficará instalado em local fixo e conhecido (IP e porta). Ele deverá receber mensagens de cadastramento de usuários (clientes) e divulgar a lista de usuários logados.

##### Os clientes deverão cadastrar um username (único) junto ao servidor, receber a lista de usuários online, enviar e receber mensagens de outros usuários.

##### Cada grupo deverá decidir se as interações ocorrerão por TCP/IP ou UDP/IP:

##### \* Entre o servidor e os clientes; e

##### \* Entre os clientes.

##### Além disso, deverão decidir se as interações entre os clientes ocorrerão diretamente entre si (peer-to-peer) ou através do servidor.

#### Escolha de pontuação adicional

#### 3.2 DESCONEXÃO (2 PONTOS)

##### Os usuários deverão descadastrar-se ao saírem do sistema. Além disso, o servidor deverá verificar se há clientes offline e removê-los de sua lista de usuários ativos.

#### 4. ENTREGA

##### \* O código fonte de todos os programas implementados;

##### Um relatório descrevendo:

##### \* O Ambiente utilizado

##### \* Descrição em alto nível dos programas, incluindo diagramas dos diferentes esquemas de interação entre clientes e servidor utilizados;

##### \* Formas (peer-to-peer ou através do servidor) e protocolos (TCP ou UDP) escolhidos para as interações, com justificativas para as escolhas;

##### \* Formato das mensagens trocadas;

##### \* Descrição dos testes realizados para verificar se o programa realiza as tarefas solicitadas.

##### \* Um vídeo com até 2 minutos mostrando o funcionamento do sistema (ou link para ele).
