# 📝 Sistema de Cadastro

## 🚀 Visão Geral

Este projeto é um **formulário de cadastro (CRUD - Create)** desenvolvido com **React + Vite** e **TypeScript**, oferecendo uma interface moderna, responsiva e altamente validada.

Além disso, foram implementados **testes automatizados com PyTest e Selenium** para garantir a integridade dos dados e comportamento do sistema.

---

## ✨ Funcionalidades

### ✅ Formulário de Cadastro com:

- Nome completo
- Telefone (com máscara)
- CPF (com máscara)
- E-mail
- Confirmação de e-mail
- Senha
- Confirmação de senha

### 🔒 Validações Reais:

- **Nome:** obrigatório, 3–50 caracteres
- **Telefone:** formato `(XX) XXXXX-XXXX`, validado por regex
- **CPF:** formato `XXX.XXX.XXX-XX`, validação de dígitos
- **E-mail:** domínio válido, confirmação
- **Senha:** entre 8 e 20 caracteres, confirmação obrigatória

### 🎨 Interface Moderna:

- Estilizada com foco em responsividade
- Feedback visual em tempo real
- Ícones e mensagens intuitivas
- Layout 100% responsivo
- Animações suaves

---

## 🧪 Testes Automatizados

Executados com `python -m pytest tests/test_registration.py -v`  
e `python -m pytest tests/test_registration_edge.py -v`

Cobrem todos os principais casos de uso:

- ✅ Validação de senha (mínimo 8 caracteres)
- ✅ Validação de telefone (formato correto)
- ✅ Validação de CPF (formato e dígitos válidos)
- ✅ Validação de e-mail (incluindo confirmação)
- ✅ Testes de sucesso (cadastro completo com dados válidos)

---

## 🛠️ Tecnologias Utilizadas

### 🎯 Frontend:

- React
- Vite
- TypeScript
- React Hook Form
- Yup (validação)

### 🧪 Testes:

- PyTest
- Selenium
- WebDriver Manager

---

## ✅ Destaques Técnicos

- **Validação em tempo real**
- **Máscaras de entrada** (telefone e CPF)
- **Confirmação de campos**
- **Feedback claro e contextual**
- **Código modular e bem estruturado**

---

## 📌 Conclusão

O sistema oferece:

- 🖥️ Interface moderna e amigável
- 🧠 Validações completas
- 🧪 Testes automatizados
- 🧰 Código limpo e de fácil manutenção

