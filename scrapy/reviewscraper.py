import scrapy
import csv

import sites

class ReviewSpider(scrapy.Spider):

    name='reviewSpider'
    start_urls = [site[1] for site in sites.get()]


    def parse(self, response):
        csvwriter = csv.writer(open('reviews.csv', 'a'))
        for review in response.css('[data-hook=review]'):
            csvwriter.writerow([
                review.css('.a-profile .a-profile-name::text').get().encode('utf-8','ignore'),
                review.css('.a-profile::attr("href")').get(),
                review.css('[data-hook=review-title] .cr-original-review-content::text').get().encode('utf-8','ignore'),
                review.css('[data-hook=review-title]::attr("href")').get().encode('utf-8','ignore'),
                review.css('[data-hook=review-body] .cr-original-review-content::text').get().encode('utf-8','ignore')
            ])

        next_page = response.css('[data-hook=pagination-bar] li.a-last a::attr("href")').get()

        if next_page is not None:
            print ("Getting next_page!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            yield response.follow(next_page, self.parse)