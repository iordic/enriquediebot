# Enriquedediebot

Se han omitido ficheros y valores por seguridad.

Reglas a añadir en crontab:
```bash
# m h  dom mon dow   command
0 */8 * * * cd PATH_HERE && python3 tweet.py
0 0 1 * *   cd PATH_HERE && python3 parser.py
0 0 2 * *   cd PATH_HERE && mv generator.bin generator.bin.old && python3 generator.py
```
