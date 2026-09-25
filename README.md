# SISGESAC - Sistema de Cadastro de Pontos de Internet e Wi-Fi

Projeto prático desenvolvido para a disciplina de **Programação Orientada a Objetos (POO)** no 2º semestre do curso de Ciência da Computação.

---

## 👥 Integrantes do Projeto

* **Arthur Moura Campos** | RA: 22602304
* **Derick Dixon Xavier Rodrigues** | RA: 22602449
* **Arthur Souza Mendes** | RA: 22600960

---

## 🧠 Conceitos de POO Aplicados

1. **Classe Abstrata:** Criação da classe-base `PontoPresenca(ABC)`, impossibilitando instanciações diretas de pontos genéricos.
2. **Encapsulamento:** Atributos estritamente privados via duplo sublinhado (`__id_gesac`, `__upload`, `__download`, `__beam`) com leitura exposta por meio de getters com `@property`.
3. **Herança:** Derivação das subclasses `PontoInternet` e `PontoWifi` a partir de `PontoPresenca`, reaproveitando o construtor base com `super().__init__()`.
4. **Sobrescrita de Métodos:** Redefinição do método `cadastrar(bd)` nas classes derivadas para atender às especificidades de cada tipo de rede.
5. **Polimorfismo:** Execução do método `cadastrar(bd)` compartilhado pela interface da classe base, disparando comportamentos distintos conforme a tecnologia.
6. **Armazenamento em Dicionários:** Mapeamento de objetos na memória utilizando o identificador `idGesac` como chave única.

---

## ⚙️ Regras de Negócio e Validações

* **Pontos de Internet:** Inserção direta no dicionário de dados após checagem de chave duplicada.
* **Pontos Wi-Fi:** Validação técnica obrigatória antes do salvamento:
  * Download mínimo: **300 Mbps**
  * Upload mínimo: **30 Mbps**
  * Chave única: Rejeição de identificadores já cadastrados na base.
* **Tratamento de Exceções:** Emprego de blocos `try-except` e emissão de alertas com `raise` para impedir interrupções inesperadas de execução.
