import scrapy  # type: ignore


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    page_count = 1
    page_max = 10

    # informa em qual site ira fazer a pesquisa
    start_urls = [
        "https://lista.mercadolivre.com.br/tenis-de-corrida-masculino"]

    def parse(self, response):
        products = response.css('div.ui-search-result__content')

        for product in products:
            prices = product.css(
                'span.andes-money-amount__fraction::text').getall()
            yield {
                'brand': product.css('span.ui-search-item__brand-discoverability.ui-search-item__group__element::text').get(),
                'name': product.css('h2.ui-search-item__title::text').get(),
                'old_price_reais': prices[0] if len(prices) > 0 else None,
                'new_price_reais': prices[0] if len(prices) > 0 else None,
                'old_price_centavos': prices[1] if len(prices) > 1 else None,
                'new_price_centavos': prices[1] if len(prices) > 1 else None,
                'reviews_rating_number': product.css('span.ui-search-reviews__rating-number::text').get(),
                'reviewa_amount': product.css('span.ui-search-reviews__amount::text').get()
            }
            
        if self.page_count < self.page_max:
             next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()
             if next_page:
                 self.page_count += 1
        yield scrapy.Request(url=next_page, callback=self.parse)
       
            

