import json
from PIL import Image, ImageChops
import os
from pathlib import Path
from datetime import datetime

adress = ["ул. Алтайская, д. 33/7", "ул. Байкальская, д. 36", "ул. Байкальская, д. 32", "ул. Байкальская, д. 26/10", "ул. Большая Черкизовская, д. 1", "ул. Халтуринская, д. 11", "ул. Просторная, д. 13", "ул. Артюхиной, д. 25", "ул. Артюхиной, д. 27", "ул. Юных Ленинцев, д. 34", "ул. Юных Ленинцев, д. 46", "ул. Ставропольская, д. 5", "ул. Шоссейная, д. 42", "ул. Гурьянова, д. 49", "ул. Довженко, д. 7", "ул. Довженко, д. 5", "ул. Алабяна, д. 15", "ул. Константина Царева, д. 4", "ул. Коптевская, д. 18", "ул. Коптевская, д. 30"]
name = ["Федоров Андрей", "Галкин Михаил", "Котов Олег", "Иванов Иван", "Петров Петр", "Дмитриев Дмитрий", "Романов Олег", "Важный Сергей", "Матросов Дмитрий", "Важный Сергий", "Кривоусов Артем", "Костылев Алекксандр", "Сергеев Сергей", "Мудрый Евгений", "Герасимов Виталий", "Суровый Эдуард", "Новиков Илья", "Павлов Иван", "Венедиктов Алексей", "Суббота Олег", "Минский Егор"]
podezd = ["5", "1", "3", "2", "4", "4", "2", "1", "1", "3", "1", "2", "1", "2", "4", "3", "3", "5", "1", "2"]
statia = ["119 УК РФ", "119 УК РФ", "112 УК РФ", "105 УК РФ", "115 УК РФ", "115 УК РФ", "105 УК РФ", "112 УК РФ", "112 УК РФ", "119 УК РФ", "105 УК РФ", "105 УК РФ", "112 УК РФ", "119 УК РФ", "105 УК РФ", "105 УК РФ", "119 УК РФ", "105 УК РФ", "112 УК РФ", "119 УК РФ"]
coord = [[55.82087723701981,37.83280055457458], [55.81636382116363,37.80629586105406], [55.81633361720102,37.80478309516965], [55.816552334290016,37.80086420396973], [55.79861820245995,37.72704604863123], [55.80162965366415,37.72491997146371], [55.80676681718039,37.72293809306556], [55.69467890286604,37.7403061868221], [55.69401232503177,37.74052076354328], [55.70060046407909,37.75597524046744], [55.70028733781756,37.760413895657045], [55.680621338925164,37.74135268470696], [55.68045727449408,37.72329815693959], [55.68097673232604,37.71690879343591], [55.72082868833446,37.51411182521413], [55.72202163804406,37.51588208316396], [55.800794358320026,37.50738333825017], [55.811042449363484,37.491452927531775], [55.83009911185524,37.51902581036108], [55.83725075647187,37.52260503346157]]
simple_path = 'C:\\'
images = ["simple_path\\01.png",
          "simple_path\\02.jpg",
          "simple_path\\03.jpg",
          "simple_path\\04.jpg",
          "simple_path\\05.jpg",
          "simple_path\\06.jpg",
          "simple_path\\07.jpg"]
who = "default"

def difference_images(img1, img2):
    global name
    global who
    image_1 = Image.open("C:\\mapofcriminal\\img\\" + img1)
    image_2 = Image.open(img2)
    size = [400, 300]  # размер в пикселях
    image_1.thumbnail(size)  # уменьшаем первое изображение
    image_2.thumbnail(size)  # уменьшаем второе изображение
    # сравниваем уменьшенные изображения
    result = ImageChops.difference(image_1, image_2).getbbox()
    if result == None:
        index_name_for_img= images.index(img2)
        print('Похож на ' +name[index_name_for_img])
        who = name[index_name_for_img]
    else:
        return 0
        #print("не похож")
    return who

def comparison(imput_text):
    global who
    for filename in os.scandir("C:\\mapofcriminal\\img1"):
        print('Сравним '+imput_text+' и '+ filename.path)
        who = difference_images(imput_text,filename.path)
        if who:
            break
    return who

def metka(who):
    global adress
    global coord
    global name
    global podezd
    global statia
    print(who)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if who!="default":
        print("Нашли, рисуем метку")
        index_name = name.index(who)
        path = Path("data.json")
        data = json.loads(path.read_text(encoding='utf-8'))
        data['features'].append({"type": "Feature", "id": 0, "geometry": {"type": "Point", "coordinates": coord[index_name]}, "properties":
                    { "hintContent": "<div class='map__hint'>Время: "+current_time+" Адрес:"+adress[index_name]+"Подъезд: "+podezd[index_name]+"</div>","balloonContentBody": "<div class='map__balloon'><p>"+name[index_name]+"Статья: "+statia[index_name]+". </p><img class='map__Andrey-img' src='file:///C:/Users/79015/PycharmProjects/mapofcriminal/img1/"+images[index_name].replace("C:\\Users\\79015\\PycharmProjects\\mapofcriminal\\img1\\","")+"' alt='Был судим. '/></div>"}})
        print(images[index_name].replace("C:\\mapofcriminal\\img",""))
        path.write_text(json.dumps(data), encoding='utf-8')

while True:
    imput_text = input("Фото с домофона")
    who = comparison(imput_text)
    metka(who)
    print('метка обновлена')
