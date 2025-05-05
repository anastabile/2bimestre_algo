def calculadora_imc (pessoa):
    imc=pessoa ["peso"]/(pessoa["altura"]*pessoa ["altura"])
    resultado= f"o imc {pessoa ["nome"]} é {imc:.2f}"
    #usando comando ternario
    saudavel= 18.5< imc < 25

    return{
        "nome": ["nome"],
        "imc": imc,
        "resultado":resultado,
        "saudavel": saudavel
    }

pessoa1={
    "nome": "jose",
    "peso": 110,
    "altura": 1.75
}

pessoa2={
    "nome": "maria",
    "peso": 55,
    "altura": 1.70
}
print(calculadora_imc(pessoa1))
print(calculadora_imc(pessoa2))

