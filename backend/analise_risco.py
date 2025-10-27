def analisar_risco(risco: str, valor: float) -> str:
    risco = risco.upper()
    if risco not in ('BX', 'AL'):
        return f'{risco} é inválido para o grau de risco'
    
    if risco == 'BX':
        tipo = 'Poupança' if valor < 1000.0 else 'Renda Fixa'
    else:
        tipo = 'Bitcoins' if valor < 1000.0 else 'Ações'
    
    return f'Você deve investir em {tipo}'
