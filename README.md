
Analisador de Currículos em Python

Este projeto é uma ferramenta em Python que lê e classifica currículos em PDF de forma automática. Ele identifica palavras-chave para categorizar cada perfil em áreas como Front-End, Back-End ou Data Science.

Funcionalidades

Extração de texto: Lê arquivos PDF usando a biblioteca PyPDF2.

Classificação inteligente: Filtra palavras-chave para determinar a área de atuação do candidato.

Saída clara: Apresenta os resultados de forma fácil de entender no terminal.

Código expansível: A estrutura foi pensada para ser simples de adaptar a modelos de Machine Learning mais complexos no futuro.


Como Usar

Clone o repositório:

Bash

git clone https://github.com/lucio734/resume-classifier.git
cd resume-classifier

Instale as dependências:


Bash

pip install PyPDF2
Adicione os currículos: Coloque seus arquivos PDF na mesma pasta do projeto.


Execute o script:


Bash

python main.py


Digite o nome do arquivo PDF quando for solicitado para ver a classificação.


Tecnologias Usadas

Python 3.x

PyPDF2 para extração de texto

VS Code como editor de código


Autor:

Lúcio Vecchio

luciovhc@gmail.com

linkedin.com/in/lucio-vecchio
