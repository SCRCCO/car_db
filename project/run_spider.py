from scrapy.cmdline import execute
import os
import sys

# Aggiungi il percorso del progetto al sys.path
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'project'))

# Imposta il file di configurazione di Scrapy
os.environ['SCRAPY_SETTINGS_MODULE'] = 'car_db.settings'

# Esegui lo spider
execute(['scrapy', 'crawl', 'spider', '-o', 'cardb.csv'])
