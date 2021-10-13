from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests

class Scraper:
    ''' Scraper Class
    '''
    def url_linker(self,total_pages = 5 , *args):
        self.urls = list()
        for page in range(1, total_pages+1):
            self.urls.append(self.url_builder(page, *args))
        return self.urls

    def url_builder(self, page = 1, *args):
        self.parms = '+'.join(args)
        self.url = f'https://www.flipkart.com/search?q={self.parms}&page={page}'
        return self.url

    def scrapper(self,urls: list, category,pages):

        self.names = list()
        self.SP = list()
        self.CP = list()
        self.rating = list()
        self.people = list()
        self.discount = list()
        self.categories = list()
        self.data = dict()
        self.pages = pages
        
        for url in urls:
            print(url)

            response = requests.get(url).content
            soup = BeautifulSoup(response, 'html.parser')
            all_blocks = soup.findAll('div', class_='_4ddWXP')
            for product in all_blocks:
                try:
                    if product.find('a', class_='s1Q9rs').get_text() and product.find('div', class_='_30jeq3').get_text() and product.find('div', class_='_3I9_wc').get_text() and product.find('div', class_='_3LWZlK').get_text() and product.find('span', class_='_2_R_DZ').get_text() and product.find('div', class_='_3Ay6Sb').get_text() and category :
                        name = product.find('a', class_='s1Q9rs').get_text()
                        self.names.append(name)
                        print("Name ",name)
                        selling_price = product.find('div', class_='_30jeq3').get_text()
                        selling_price = str(selling_price).replace(",","").split("₹")[1]
                        self.SP.append(selling_price)
                        print("Sell p ",selling_price)
                        cost_price = product.find('div', class_='_3I9_wc').get_text()
                        cost_price = str(cost_price).replace(",","").split("₹")[1]
                        if cost_price :
                            self.CP.append(cost_price)
                        else:
                            self.CP.append("None")
                        print("Cost p ",cost_price)
                        rat = product.find('div', class_='_3LWZlK').get_text()
                        if rat :
                            self.rating.append(rat)
                        else:
                            self.rating.append("None")
                        print("Rating ",rat)
                        peps = product.find('span', class_='_2_R_DZ').get_text()
                        peps = str(peps).replace("(","").replace(")","").replace(",","")
                        if peps :
                            self.people.append(str(peps))
                        else:
                            self.people.append("None")
                        print("reviews ",peps)
                        disc = product.find('div', class_='_3Ay6Sb').get_text()
                        if disc :
                            self.discount.append(disc)
                        else:
                            self.discount.append("None")
                        print("Discount ",disc)
                        if category :
                            self.categories.append(category)
                        else:
                            self.categories.append("None")
                        print("Category ", category)
                except Exception as e:
                    continue
        
        self.data['names'] = self.names
        self.data['selling_price'] = self.SP
        self.data['cost_price'] = self.CP
        self.data['rating'] = self.rating
        self.data['total_rating'] = self.people
        self.data['discount'] = self.discount
        self.data['categories'] = self.categories

        
        return self.data

    def flipkart_scraper(self,category, sex, pages=10):
        self.pages = pages
        self.category = category
        self.sex = sex
        urls = self.url_linker(self.pages, self.category, self.sex)
        return self.scrapper(urls, self.category,self.pages)

    def types(self,n):
        self.n = n
        return self.n

    def dataframe_and_scrap(self,cat,pa = 5):
        '''Scraped Data and DataFrame
        '''
        df = pd.DataFrame(
                columns=[
                    'names', 
                    'categories',
                    'selling_price',
                    'cost_price',
                    'rating',
                    'discount',
                ],
            )
        df = df.rename_axis('S. No.')
        self.all_data = list()
        self.gender = 'Female'
        self.catego = self.types(f"{cat}")
        self.pag = pa
        
        data = Scraper().flipkart_scraper(self.catego,self.gender,self.pag)
        self.all_data.append(data)
        for d in self.all_data:
            df1 = pd.DataFrame(d)
            df = pd.concat([df, df1], ignore_index=True)
        return df        
#df2 = Scraper().dataframe_and_scrap("soap",2)
#print(df2)