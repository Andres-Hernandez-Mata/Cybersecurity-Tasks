"""
Uso: Web scraping
Creado: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 10 Mayo 2020
"""

from scraping import scraping

if __name__ == "__main__":
	url = 'http://www.google.es'
	scraping = Scraping()
	scraping.scrapingImages(url)
	scraping.scrapingPDF(url)
	scraping.scrapingLinks(url)
	scraping.scrapingBeautifulSoup(url)
