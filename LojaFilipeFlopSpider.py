## Aluno: JOAB TORRES ALENCAR
## Turma: TADS2015 - TARDE - SEXTO SEMESTRE
## Script: MINERACAO DE DADOS NO WEBSITE www.filipeflop.com
## versao: 1.0
## Descricao: Este script tem como objetivo realizar uma mineracao de dados por categorias do website do filipeflop, a categora escolhida deve ser informada na variavel 'category' e com isso o script ira retorna todos os produtos com 'nome do produto', 'link', 'categoria do produto' e 'valor'.
## 		OBSERVACAO: para executa este script digite o seguinte comando no terminal:
##	 	scrapy runspider LojaFilipeFlopSpider.py -o filipeflop.csv
import scrapy
class LojaSpider(scrapy.Spider):
	name = "felipeflop"
	category = "arduino/acessorios-arduino/" #categoria escolhida para mineracao
	start_urls = ["https://www.filipeflop.com/categoria/%s" % category] 
	
	def parse(self, response):
		for product in response.css('li.product'):
			yield{		
				'valor' : product.css('.amount::text').extract_first(),
				'url' : product.css('.woocommerce-loop-product__link::attr(href)').extract_first(),
				'produto' : product.css('.woocommerce-loop-product__title::text').extract_first(),
				'categoria': product.css('.loop-product-categories a::text').extract(),
			}
			
		link_next = response.css('ul.page-numbers li a.next::attr(href)').extract_first()
		if link_next:
			yield scrapy.Request(response.urljoin(link_next))

