import scrapy

class LojaFilipeFlop(scrapy.Spider):
	name = "filipeflop"
	start_urls = ['https://www.filipeflop.com/']
	
	def parse(self, response):
		
		for category in response.css('div.wpb_wrapper ul li'):
			yield{
				'link' : category.css('a::attr(href)').extract_first(),
				}
				
f = LojaFilipeFlop()
f.parse('https://www.filipeflop.com/')
