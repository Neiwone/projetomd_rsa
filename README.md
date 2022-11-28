# Criptografia RSA | Matemática Discreta

Projeto final da matéria de Matemática Discreta
Feito por Vinícius da Costa Neitzke (vcn@ic.ufal.br).


# Como executar

Para executar instale o python 3 na sua máquina caso ainda não o tenha, e então, execute o comando:
```sh
python projetomd_rsa.py
```

Feito isso vai aparecer 3 opções, primeiramente gere a chave pública (digitando 1).

Em seguida você já pode criptografar (digitando 2) ou descriptografar (digitando 3) qualquer trecho desejado.
  - por favor atentar a remover caracteres inválidos, são apenas validos letras na hora de encriptar.

Em todas opcões, os resultados são salvos em um respectivo arquivo de texto no mesmo diretorio onde se encontra o codigo

# Como funciona
## Gerar chave pública
  Para gerar a chave pública são necessários:
  
  -  Um par de primos _p_ e _q_;
  
  -  Um expoente _e_ que seja relativamente primo a (_p_-1)(_q_-1);

## Encriptar
  Para criptografar a mensagem, é utilizado a formula:
  ```sh
  c = m^e mod n
  ```
  Em que :
  
  -  _m_ é um caractere;
    
  -  _e_ é o primo entre si de _phi(n)_;
  
  -  _phi(n)_ é (_p_-1)(_q_-1);
     
  -  _n_ é a multiplicação de _p_ e _q_;
   
  -  _c_ é o caractere criptografado.
   
## Descriptar
   Para descriptografar a mensagem, utilizamos a fórmula
  ```sh
  m = c^d mod n
  ```
  Em que :
  
  -  _c_ é o caractere a ser descriptografado em formato de número;
   
  -  _d_ é o inverso de _e_ calculado como:     
  ```sh
  e*d mod phi(n) = 1
  ```
  -  _n_ é a multiplicação de _p_ e _q_;
   
  -  _m_ é o caractere descriptografado.
    
