# Grande Sábio
Grande sábio é um protótipo de assistente virtual desenvolvido completamente por
Samuel Santos. Esse protótipo foi desenvolvido utilizando python e suas bibliotecas.
Inicialmente esse assistente deve entender comandos de voz e os direcionar para
o sujeito e a ação específica. Futuramente a intenção é expandir para que comandos
visuais e escritos também sejam interpretados.

## Conceitos Importantes

### Sujeito
Sujeito é considerado tudo que irá receber o comando. Seria o local (como "sala",
"cozinha" ou "banheiro"), o alvo mais específico (como minha "contabilidade") ou
objetos (como "drone" ou "robô").

### Verbos
Cada sujeito terá seus próprios métodos ou funções, sendo assim, "verbo" seria a
função que será chamada a partir do comando inicial.

### Parâmetros
Após o Sujeito e a função serem definidas, "parâmetros" serão tudo que estiver
restante no comando inicial e que possa ser relevante para o funcionamento desejado 
do comando.

### Base
O Diretório "base" inclui as funções e bibliotecas que podem ser consideradas pré-requisitos
para uma determinada ação de um sujeito. Por exemplo:
Para acessar uma página automaticamente eu irei precisar do WebDriverManager, então
ao invés de criar um código separado para cada sujeito, irei inserir isso como base.
Assim vários sujeitos que necessitam acessar uma pagina podem utilizar a mesma base.

