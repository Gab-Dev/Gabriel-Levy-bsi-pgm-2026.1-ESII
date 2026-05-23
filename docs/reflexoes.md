## Aula 04 — SRP
A decisão mais difícil foi separar a responsabilidade de notificação do ServicoEmprestimo. Inicialmente parecia mais simples deixar os prints de e-mail dentro da própria lógica de negócio, porque o envio acontece durante o empréstimo. Porém, analisando o princípio SRP discutido por Valente no Capítulo 5, percebi que isso criaria dois motivos diferentes para alteração na mesma classe: mudanças na regra de negócio e mudanças na notificação.
A separação exigiu pensar melhor sobre as fronteiras entre os componentes e aumentou um pouco o número de arquivos, mas trouxe mais organização e clareza para o sistema. O critério utilizado foi justamente o conceito de responsabilidade única apresentado por Valente, buscando garantir maior coesão e menor acoplamento entre os módulos.


## Aula 05 — OCP
A aplicação do OCP através de polimorfismo melhorou a organização do sistema, pois cada tipo de equipamento passou a ser responsável pelo próprio cálculo de multa. Isso eliminou os blocos de if/elif do serviço e reduziu o acoplamento entre as regras de negócio e os tipos específicos de equipamento.
Entretanto, como discutido por Valente no Capítulo 5, o OCP possui limites. Caso surgisse um requisito muito diferente, como multas calculadas por hora ou dependendo do dia da semana, talvez a hierarquia atual não fosse suficiente. Nesse cenário, seria necessário repensar a decomposição, possivelmente utilizando estratégias ou composição em vez de apenas herança.
Portanto, o OCP funciona bem para variações previsíveis, mas não elimina totalmente futuras modificações arquiteturais quando os requisitos mudam de forma radical.


## Aula 06 — Verificação de LSP
As subclasses Notebook, Projetor e Camera respeitam o contrato definido pela classe base Equipamento.
O método calcular_multa(0) retorna 0 em todas as subclasses, pois o cálculo utiliza max(0, valor), impedindo valores negativos.
Da mesma forma, calcular_multa(-5) também retorna 0, garantindo que nenhuma multa negativa seja produzida.
Nenhuma das subclasses lança exceções inesperadas durante o cálculo, desde que o parâmetro informado seja numérico. Assim, todas mantêm o contrato estabelecido pela classe abstrata, que exige retorno do tipo float ou inteiro maior ou igual a zero.
Portanto, o princípio LSP (Liskov Substitution Principle) é satisfeito, pois qualquer subclasse pode substituir Equipamento sem quebrar o comportamento esperado pelo ServicoEmprestimo.

## Aula 06 — DIP
A aplicação do DIP alterou significativamente a relação de dependência entre os módulos do sistema. Antes, o ServicoEmprestimo criava diretamente suas dependências, ficando fortemente acoplado ao RepositorioEmprestimo e ao Notificador. Isso dificultava alterações, reutilização e principalmente testes isolados.
Com a inversão de dependência, o serviço deixou de controlar a criação desses objetos e passou apenas a utilizá-los. Agora as dependências são fornecidas externamente pelo main.py, tornando o serviço mais flexível e desacoplado.
Na prática, a mudança não foi apenas técnica, como adicionar parâmetros no construtor, mas também conceitual. O controle da criação dos objetos foi invertido. O ServicoEmprestimo deixou de “mandar” nas dependências e passou a depender apenas das funcionalidades que recebe.
Segundo Valente, no Capítulo 5 de Engenharia de Software Moderna, a inversão de dependência reduz acoplamento e melhora a testabilidade do sistema. Isso ficou evidente ao permitir a criação de repositórios e notificadores falsos sem necessidade de alterar a lógica principal do serviço.