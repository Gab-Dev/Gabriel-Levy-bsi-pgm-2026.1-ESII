# ADR-001 — Decisão de Arquitetura

## Contexto
O sistema precisa atender dois requisitos principais:

- RNF03: permitir adicionar novos tipos sem modificar múltiplos módulos
- RNF04: permitir testar regras sem depender de estado externo

O código atual (emprestimos.py) está todo em um único arquivo, dificultando manutenção e testes.

## Opções consideradas

### 1. Arquivo único
- Simples de entender
- Difícil de manter
- Não atende RNF03 nem RNF04

### 2. Arquitetura em camadas (MVC)
- Separação entre lógica, controle e interface
- Facilita testes
- Permite evolução do sistema
- Atende RNF03 e RNF04

## Decisão
Será utilizada uma arquitetura em camadas, organizada da seguinte forma:

- `models/` → regras de negócio
- `services/` → lógica da aplicação
- `controllers/` → controle do fluxo
- `cli/` → interface do usuário
- `main.py` → ponto de entrada

## Consequências

### Positivas:
- Código mais organizado
- Facilita testes
- Permite adicionar funcionalidades facilmente

### Negativas:
- Estrutura mais complexa para iniciantes


## Avaliação dos estilos arquiteturais

| Critério | Arquivo único | Em camadas (MVC) |
|---------|-------------|------------------|
| Atende RNF03? | ❌ Não | ✅ Sim |
| Atende RNF04? | ❌ Não | ✅ Sim |
| Adequado para CLI? | ✅ Sim | ✅ Sim |
| Familiar para iniciantes? | ✅ Sim | ⚠️ Médio |