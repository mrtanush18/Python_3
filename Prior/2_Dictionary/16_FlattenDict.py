dict = {"ide":"001","name":"sunrise",
"img":{"url": "images/001.jpg",
"thumbnail":{"url":"images/thumbnails/001.jpg","height,width":"2x4"}}}

# Make dict flat/simple Convert nested dictionary to simple. ex.new_dict = {} 

new_dict = {}

for key,value in dict.items():
    if key == "img":
        new_dict["img_url"] = dict["img"]["url"]
        new_dict["img_url_thumbnail"] = dict["img"]["thumbnail"]["url"]
        new_dict["img_url_thumbnail_height,width"] = dict["img"]["thumbnail"]["height,width"]
    if key != "img":
        new_dict[key] = value

print(new_dict)

# o/p :
# {'ide': '001', 'name': 'sunrise', 'img_url': 'images/001.jpg', 'img_url_thumbnail': 'images/thumbnails/001.jpg', 'img_url_thumbnail_height,width': '2x4'}
