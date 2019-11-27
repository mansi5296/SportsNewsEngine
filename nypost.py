import scrapy

class NypostSpider(scrapy.Spider):
    name = "nypost"
    allowed_domains = ['nypost.com']
    start_urls = [
        'https://nypost.com/2018/12/01/mets-would-land-closer-with-big-set-of-cojones-in-mariners-deal/',
        'https://nypost.com/2018/12/01/money-going-to-puzzling-ends-at-mlb-and-rutgers/',
        'https://nypost.com/2018/12/01/shamorie-ponds-leads-furious-rally-to-keep-st-johns-perfect/',
        'https://nypost.com/2018/12/01/seton-halls-offense-goes-quiet-late-in-ugly-loss-to-louisville/',
        'https://nypost.com/2018/12/01/nfl-needs-more-than-talk-to-curb-its-helmet-to-helmet-problem/',
        'https://nypost.com/2018/12/01/the-nl-east-is-baseballs-most-intriguing-division/',
        'https://nypost.com/2018/12/01/dez-bryant-deletes-instagram-post-putting-him-on-team-kareem/',
        'https://nypost.com/2018/12/01/former-nba-star-sues-united-airlines-over-in-flight-race-baiting/',
        'https://nypost.com/2018/12/01/ohio-state-vs-northwestern-buckeyes-arent-going-to-cover-this-big-number/',
        'https://nypost.com/2018/12/01/california-predicted-to-beat-stanford-in-ugly-game/',
        'https://nypost.com/2018/12/01/georgia-vs-alabama-why-bulldogs-are-predicted-to-cover/',
        'https://nypost.com/2018/12/01/mets-mariners-trade-is-latest-lesson-in-naming-a-deals-winner/',
        'https://nypost.com/2018/12/01/tracing-how-giants-offensive-line-crumbled-around-manning/',
    ]
    global visited_url
    visited_url = set()

    def parse(self, response):
        global visited_url
        if response.url not in visited_url:
            visited_url.add(response.url)
            # write code to process the items.
            body1 = response.css('div.entry-content p *::text').extract()
            body2 = ''
            
            for eachString in body1:
                body2 += eachString
            

            title1 = response.css('h1 a::text').extract()
            title2 = ''

            for eachString in title1:
                title2 += eachString

            title2 = title2.strip()


            author1 = response.css('p.byline a::text').extract()
            author2 = ''

            for eachString in author1:
                author2 += eachString

            author2 = author2.strip()

       
            date1 = response.css('p.byline-date::text').extract()
            date2 = ''

            for eachString in date1:
                date2 += eachString
                
            date2 = date2.strip()

            yield {
                'url': response.url,
                'body': body2,
                'title': title2,
                'author': author2,
                'date': date2,
            }
            
            links = response.css('h5.trending-story__headline a::attr(href)').extract()
            for item in links:
                #if item.find(" ") is 0:
                yield response.follow (item, callback=self.parse)


