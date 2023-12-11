# coding: utf-8
import json
import os
file_path = os.path.abspath('latLon.txt')

with open(file_path, 'r') as text_file:
    lines = text_file.read()
    
result_list = []

for line in lines.split('\n'):
    if line.strip():  # Đảm bảo không xử lý các dòng trống
        lat, lon = map(float, line.split())
        result_list.append({"lat": lat, "lon": lon})

file_path = "locationData.json"
with open(file_path, 'w') as json_file:
    json.dump(result_list, json_file,indent=4)
