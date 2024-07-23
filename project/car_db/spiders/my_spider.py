import scrapy

class MySpider(scrapy.Spider):
    name = 'spider'
    start_urls = [
        'https://www.autoscout24.it/lst',
    ]

    def parse(self, response):
        # Estrae i link alle pagine di dettaglio dei veicoli
        print(response.css('div.ListPage_container__Optya'))
        for car in response.css('div.cldt-summary-full-item'):
            detail_page = car.css('a::attr(href)').get()
            if detail_page is not None:
                yield response.follow(detail_page, self.parse_car)
        
        # Segue il link alla pagina successiva, se esiste
        next_page = response.css('li.sds-pagination__item a.sds-button--next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
    
    def parse_car(self, response):
        # Estrazione dei dati dalla pagina di dettaglio del veicolo
        yield {
            'title': response.css('h1.cldt-detail-title::text').get(),
            'price': response.css('span.cldt-price::text').get(),
            'mileage': response.css('span.cldt-stage-primary-keyfact::text').get(),
            'registration_date': response.css('span.cldt-stage-primary-keyfact::text')[1].get(),
            'power': response.css('span.cldt-stage-primary-keyfact::text')[2].get(),
        }
