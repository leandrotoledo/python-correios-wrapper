# Correios RESTful API

## Consultar CEP

### Parâmetros

[http://localhost:5000/consultacep/](http://localhost:5000/consultacep/)

### Exemplo

```json
{
  "bairro": "Santa Cecília",
  "cep": "01230000",
  "cidade": "São Paulo",
  "complemento": null,
  "complemento2": "- lado par",
  "end": "Rua Doutor Albuquerque Lins",
  "id": null,
  "uf": "SP"
}
```

## Rastrear Encomenda

### Parâmetros

[http://localhost:5000/rastreamento/](http://localhost:5000/rastreamento/)

### Exemplo

```json
...
  {
    "cidade": "MIRANDIBA",
    "codigo": 56980971,
    "data": "18/03/2016",
    "descricao": "Objeto, ainda, não chegou na unidade.",
    "detalhe": "Por favor, aguarde.",
    "hora": "15:43",
    "local": "AGC VILA DE CACHOEIRINHA",
    "status": "09",
    "tipo": "BDR",
    "uf": "PE"
  },
...
```
