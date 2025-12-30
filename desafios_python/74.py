#tupla de ordens do time do brasileirao

times='Atlético-MG', 'Bahia', 'Botafogo', 'Bragantino', 'Ceará', 'Corinthians', 'Cruzeiro', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Mirassol', 'Palmeiras', 'Santos', 'São Paulo', 'Sport', 'Vasco', 'Vitória'

print(f'os 5 primerios times são {times[:5]}\n')
print(f'os 4 ultimos colocados são {times[-4:]}\n')

print(f'os times em ordem alfabetica sao {sorted(times)}\n')
print(f'o inter ta na psoição {times.index('Internacional')+1   }\n')