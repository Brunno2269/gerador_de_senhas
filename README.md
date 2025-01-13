# Gerador de Senhas Seguras

## Descrição
Um aplicativo Python que gera senhas seguras e customizáveis. Ideal para quem deseja manter suas contas protegidas com senhas fortes.

## Funcionalidades
- Opções para incluir ou excluir caracteres maiúsculos, números e símbolos.
- Escolha personalizada do comprimento da senha.
- Possibilidade de salvar as senhas geradas em um arquivo.

## Como Usar
1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd password_generator
   ```
2. Execute o programa:
   ```bash
   python password_generator.py -l 16 -f passwords.txt
   ```
   - `-l`: Define o comprimento da senha.
   - `-f`: Especifica o arquivo para salvar a senha.

## Exemplo
Gerar uma senha de 20 caracteres sem símbolos:
```bash
python password_generator.py -l 20 --no-symbols
```

## Requisitos
- Python 3.7 ou superior.

## Estrutura do Projeto
```
password_generator/
├── password_generator.py  # Código principal do aplicativo.
├── README.md              # Documentação do projeto.
├── requirements.txt       # Dependências do projeto.
├── .gitignore             # Arquivos e pastas a serem ignorados pelo Git.
```

## Contribuição
Contribuições são bem-vindas! Abra um pull request com suas melhorias ou ideias.

## Licença
Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais informações.
