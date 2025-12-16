# Atividade-de-valida-o-dos-pilares-de-POO
<img width="497" height="261" alt="Diagrama sem nome drawio (1)" src="https://github.com/user-attachments/assets/4094d572-65d5-476b-b2d9-ed4ba2c95e90" />
# 🌳 Sistema de Catalogação de Árvores

## 📋 Descrição

Este é um sistema interativo de catalogação de árvores desenvolvido em Python. O programa permite ao usuário registrar informações detalhadas sobre árvores, incluindo características físicas, tipo de fruta (se aplicável) e a estação do ano atual.

## 🏗️ Estrutura do Projeto

O projeto é composto por dois arquivos principais:

### 1. `classes.py` - Definição das Classes

#### Classe `Arvore`
Classe base que representa uma árvore genérica com os seguintes atributos:
- **nome**: Nome da árvore
- **folhas**: Cor das folhas ou indicação de ausência
- **tronco**: Cor do tronco
- **calendario_climatico**: Estação do ano (inverno ou verão)

#### Classe `ArvoreFrutiferas`
Classe que herda de `Arvore` e adiciona:
- **frutas**: Nome da fruta produzida pela árvore

### 2. `interface.py` - Interface do Usuário

Arquivo principal que contém a função `menu()` responsável pela interação com o usuário.

## 🎯 Funcionalidades

### Sistema de Validação Robusta

O programa utiliza loops `while True` para garantir que todas as entradas do usuário sejam válidas:

1. **Validação de Nome**: Aceita qualquer nome digitado
2. **Validação de Frutífera**: Verifica se a árvore produz frutas
3. **Validação de Folhas**: Confirma presença e cor das folhas
4. **Validação de Tronco**: Verifica cor dentro das opções disponíveis
5. **Validação de Estação**: Determina automaticamente a estação baseada no mês

### Opções Disponíveis

**Cores de Folhas:**
- verde
- marron
- vermelho
- laranja
- sem folhas

**Cores de Tronco:**
- branco
- marron
- cinza
- arco-iris
- vermelho

**Meses e Estações:**
- **Inverno**: janeiro a julho
- **Verão**: agosto a dezembro

## 🔄 Fluxo do Programa

```
Início
  ↓
Nome da Árvore
  ↓
É Frutífera? → [Sim] → Qual fruta?
             → [Não] → "não frutífera"
  ↓
Tem Folhas? → [Sim] → Qual cor? (validação)
            → [Não] → "sem folhas"
  ↓
Cor do Tronco (validação)
  ↓
Mês Atual (determina estação automaticamente)
  ↓
Exibe Status da Árvore
```

## 💻 Como Usar

1. Execute o arquivo `interface.py`:
```bash
python interface.py
```

2. Siga as instruções na tela:
   - Digite o nome da árvore
   - Responda se é frutífera (sim/não)
   - Informe se tem folhas e qual a cor
   - Escolha a cor do tronco
   - Indique o mês atual

3. O sistema exibirá um resumo completo:
```
------------| Status |------------
nome: Mangueira
folhas: verde
fruta: manga
tronco: marron
estação: verão
```

## 🎓 Conceitos de Programação Utilizados

### 1. **Orientação a Objetos**
- Classes e Herança
- Instanciação de objetos
- Atributos de classe

### 2. **Estruturas de Controle**
- Loops `while` para validação
- Estruturas condicionais `if/elif/else`
- Comandos `break` e `continue`

### 3. **Validação de Entrada**
- Verificação de dados com listas
- Tratamento de respostas do usuário
- Feedback de erros

### 4. **Lógica de Negócio**
- Determinação automática de estação por mês
- Tratamento condicional de atributos (frutífera/não frutífera)
- Validação em cascata (folhas → cor)

## 🐛 Observações Técnicas

### Pontos Fortes
- ✅ Validação robusta de entradas
- ✅ Interface amigável com feedback claro
- ✅ Uso de loops para garantir dados válidos
- ✅ Estrutura modular (separação de classes e interface)

### Possíveis Melhorias
- Considerar uso de `.lower()` para tornar entradas case-insensitive
- Adicionar opção de cadastrar múltiplas árvores
- Implementar salvamento de dados em arquivo
- Corrigir a herança em `ArvoreFrutiferas` (não chama `super().__init__()`)

## 📝 Exemplo de Uso

```
Olá bem vindo ao site de arvores, aqui nos catalogamos
        sua arvore e armazenamos no sistema:
Digite o nome da arvore: Ipê Roxo
A arvore é frutifera? não
A arvore tem folhas? sim
Qual a cor das folhas? verde
Qual a cor do tronco? marron
Em que mês estamos? setembro

------------| Status |------------
nome: Ipê Roxo
folhas: verde
fruta: não frutifera
tronco: marron
estação: verão
´´´
