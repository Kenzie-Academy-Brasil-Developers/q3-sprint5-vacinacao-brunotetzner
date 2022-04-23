# Entrega Vacinação

### Projeto com a proposta de documentar os dados de pessoas vacinadas.

&nbsp;

# Criando um registro de vacinação

### **POST** baseURL/_vaccinations_

Insira cpf, nome do individuo, nome da vacina e do posto de saúde no corpo da requisição, como no exemplo abaixo.

```json
{
  "cpf": "12345678910",
  "name": "John Doe",
  "vaccine_name": "coranavac",
  "health_unit_name": "posto municipal de Vila velha"
}
```

Atente-se ao fato de que o **CPF** é uma chave com valor unico. Ou seja, não pode se repetir.

## Retorno esperado:

```json
{
  "cpf": "12345678910",
  "name": "John Doe",
  "vaccine_name": "coranavac",
  "health_unit_name": "posto municipal de Vila velha",
  "first_shot_data": "Sat, 23 Apr 2022 00:00:00 GMT",
  "second_shot_data": "Fri, 22 Jul 2022 00:00:00 GMT"
}
```

As chaves first_shot_date e second_shot_data. Respectivamente data da primeira dose e data da segunda dose. São geradas automaticamente pela aplicação.

&nbsp;

# Buscando todas as vacinas:

### **GET** baseURL/_vaccinations_

## Retorno esperado:

Retorna todos os registros na forma de uma lista de dicionários.

```json
[
  {
    "cpf": "12345678910",
    "name": "Jon Snow",
    "vaccine_name": "coranavac",
    "health_unit_name": "posto municipal de Vila velha",
    "first_shot_data": "Sat, 23 Apr 2022 00:00:00 GMT",
    "second_shot_data": "Fri, 22 Jul 2022 00:00:00 GMT"
  },
  {
    "cpf": "12995678911",
    "name": "Harry Potter",
    "vaccine_name": "Pfizer",
    "health_unit_name": "Ala Hospitalar de Hogwarts",
    "first_shot_data": "Sat, 23 Apr 1998 00:00:00 GMT",
    "second_shot_data": "Fri, 22 Jul 1998 00:00:00 GMT"
  },
  {
    "cpf": "12346678910",
    "name": "Thor Odinson",
    "vaccine_name": "Coronavac",
    "health_unit_name": "Setor medico da torre dos vingadores, New York",
    "first_shot_data": "Sat, 23 Apr 2012 00:00:00 GMT",
    "second_shot_data": "Fri, 22 Jul 2012 00:00:00 GMT"
  }
]
```
