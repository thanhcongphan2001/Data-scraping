# -*- coding: utf-8 -*-
import scrapy
import json
import os

class MainSpider(scrapy.Spider):
    file_path = os.path.abspath('locationData.json')
    with open(file_path, 'r') as json_file:
        datas = json.load(json_file)
        print(datas)
    name = "main"
    allowed_domains = []
    # start_urls = ['https://nominatim.openstreetmap.org/reverse?lat={}&lon={}&format=jsonv2'.format(i['lat'], i['lon']) for i in datas]
    start_urls = ['https://api-app.map4d.vn/map/geocode?lat={}&lng={}'.format(i['lat'], i['lon']) for i in datas]
    # start_urls = ['https://jsonplaceholder.typicode.com/todos/{}'.format(i) for i in range(1, 10)]
    # start_urls = ['https://api.vdtdata.com/idunn/v1/places/latlon:10.7551875:106.6860625?lang=vi']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, errback=self.error_handler)
     
    def parse(self, response):
        data = json.loads(response.text)
        # Đọc dữ liệu hiện tại từ file (nếu có)
        current_data = []
        try:
            with open('Crawl.json', 'r', encoding='utf-8') as file:
                current_data = json.load(file)
        except FileNotFoundError:
            pass  # Nếu file không tồn tại, tiếp tục với mảng trống
        # Thêm dữ liệu mới vào mảng hiện tại
        current_data.append(data)
        print(">>>>>>>>>>>>>>>>>>>>>>>",current_data)
        # Ghi mảng vào file
        with open('Crawl.json', 'w', encoding="utf-8") as file:
            json.dump(current_data, file, indent=4, ensure_ascii=False)
 
    def error_handler(self, failure):
        request_url = failure.request.url
        status_code = failure.value.response.status
        print("An error occurred for URL {request_url}: Status Code {status_code}")
        current_data = []
        try:
            with open('Status_400.json', 'r') as file:
                current_data = json.load(file)
        except FileNotFoundError:
            pass  # Nếu file không tồn tại, tiếp tục với mảng trống

        # Thêm dữ liệu mới vào mảng hiện tại
        current_data.append({'errapi': request_url, 'status': status_code})

        # Ghi mảng vào file
        with open('400_cong.json', 'w') as file:
            json.dump(current_data, file, indent=4)


