# Correios RESTful API

## Consultar CEP

### Exemplo

[http://localhost:5000/consultacep/01230000](http://localhost:5000/consultacep/01230000)

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

### Exemplo

[http://localhost:5000/rastreamento/TE123456785AA](http://localhost:5000/rastreamento/TE123456785AA)

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
