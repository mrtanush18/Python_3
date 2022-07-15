dict = {"ide":"001","name":"sunrise",
"img":{"url": "images/001.jpg",
"thumbnail":{"url":"images/thumbnails/001.jpg","height,width":"2x4"}}}

from cherrypicker import CherryPicker

result = CherryPicker(dict)

print(result.flatten().get())

# o/p :
# {'ide': '001', 'name': 'sunrise', 'img_url': 'images/001.jpg', 'img_url_thumbnail': 'images/thumbnails/001.jpg', 'img_url_thumbnail_height,width': '2x4'}