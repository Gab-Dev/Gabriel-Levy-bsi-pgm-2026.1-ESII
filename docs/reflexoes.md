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



## Aula 08 — Testes

O teste de integração consegue validar a comunicação entre múltiplos componentes reais do sistema, como o serviço, o repositório e o notificador. Isso permite detectar problemas de integração que testes unitários isolados normalmente não identificam, como incompatibilidades entre objetos, erros de persistência ou falhas no fluxo completo da aplicação.

Por outro lado, testes de integração possuem menor isolamento e dificultam identificar exatamente qual componente causou uma falha. Já os testes unitários conseguem validar regras específicas de forma mais rápida, simples e previsível, utilizando dublês para controlar dependências externas.

Portanto, testes unitários e de integração possuem objetivos diferentes e complementares. Os unitários garantem precisão no comportamento isolado das unidades, enquanto os de integração validam a colaboração real entre os módulos do sistema.


## Aula 10 – Factory e Facade

A aplicação do padrão Factory permitiu centralizar a criação dos equipamentos em uma única classe responsável por instanciar os objetos corretos. Isso reduz o acoplamento do repositório com as classes concretas e facilita a inclusão de novos tipos de equipamentos no futuro.

Já o padrão Facade simplificou a utilização do sistema ao fornecer uma interface única para as operações de empréstimo, devolução, listagem de atrasados e cálculo de multas. Com isso, o arquivo principal da aplicação passou a depender apenas da fachada, sem conhecer detalhes internos da implementação.

Esses padrões contribuem para um código mais organizado, com responsabilidades melhor definidas, facilitando manutenção, testes e evolução do sistema.


## Aula 11 - Decorator e Observer

Durante esta atividade foi possível perceber na prática como os padrões de projeto ajudam a melhorar a organização do código. No padrão Decorator, a principal vantagem foi conseguir adicionar novas funcionalidades aos equipamentos, como seguro e rastreador, sem precisar alterar as classes existentes. Isso torna o sistema mais flexível, já que novas funcionalidades podem ser adicionadas futuramente de forma simples.

Já no padrão Observer, a principal mudança foi retirar a responsabilidade de notificação do serviço de empréstimos. Antes ele chamava diretamente o notificador, ficando dependente dessa classe. Com o Observer, o serviço apenas dispara um evento e qualquer classe registrada como observadora pode receber essa informação. Isso deixa o código menos acoplado e facilita a inclusão de novos tipos de notificações no futuro, como envio de SMS ou mensagens por aplicativo.

Na minha opinião, o maior desafio foi entender como os eventos seriam enviados para os observers e adaptar o código que já existia sem quebrar os testes. Depois de implementar e executar os testes, ficou mais fácil compreender o funcionamento desses padrões e perceber como eles tornam o sistema mais organizado, reutilizável e fácil de manter.