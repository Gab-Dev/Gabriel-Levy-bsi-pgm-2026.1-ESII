# Problemas Identificados — Leitura Inicial do Código

Este arquivo é preenchido pelos estudantes na Aula 1 após a leitura do código legado.
Descreva em linguagem livre tudo que parecer estranho, errado ou difícil de entender.
Não é necessário usar termos técnicos neste momento.

---

## Minha leitura inicial

*(Espaço reservado para o estudante preencher)*

1. **Uso de variáveis globais**
   O sistema usa listas globais (`equipamentos` e `emprestimos_registrados`) diretamente dentro da classe. Isso é estranho porque dificulta o controle dos dados e pode gerar erros quando o sistema crescer. O esperado seria que esses dados ficassem organizados dentro de uma estrutura própria.

---

2. **Mistura de responsabilidades**
   A mesma classe (`Sistema`) faz tudo: controla regras de negócio, calcula multa e ainda envia “email” (print). Isso parece errado, porque cada parte deveria ter sua própria função separada.

---

3. **Cálculo de multa repetido**
   A lógica de cálculo de multa aparece mais de uma vez no código. Isso é um problema porque, se precisar mudar a regra, teria que alterar em vários lugares — aumentando a chance de erro.

---

4. **Uso de muitos `if/elif` para regras**
   O cálculo da multa depende de vários `if/elif` para cada tipo de equipamento. Isso não é muito flexível. Se aparecer um novo tipo de equipamento, o código precisa ser modificado, o que não é ideal.

---

5. **Notificações misturadas com lógica**
   O sistema imprime mensagens de “email” diretamente dentro das funções principais. Isso deixa o código bagunçado e difícil de reaproveitar, já que a lógica principal fica misturada com saída de dados.

---

6. **Falta de separação entre interface e sistema**
   O menu (`main`) está no mesmo arquivo e diretamente ligado à lógica do sistema. Isso dificulta, por exemplo, transformar o sistema em um site ou aplicativo no futuro.

## Revisão com vocabulário técnico

*(Este espaço será preenchido após a Aula 4, quando os termos técnicos corretos forem aprendidos)*
