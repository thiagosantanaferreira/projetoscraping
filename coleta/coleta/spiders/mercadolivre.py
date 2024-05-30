import scrapy  # type: ignore


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]

    # informa em qual site ira fazer a pesquisa
    start_urls = [
        "https://lista.mercadolivre.com.br/tenis-de-corrida-masculino"]

    def parse(self, response):
        products = response.css('div.ui-search-result__content')

        for product in products:
            yield {
                'brand': product.css('span.ui-search-item__brand-discoverability.ui-search-item__group__element::text').get()
            }
            

