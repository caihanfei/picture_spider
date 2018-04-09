import urllib


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []   
    
    def collect_data(self,photos):
        if photos is None:
            return
        for photo in photos:
            self.datas.append(photo)
        

    def downAllphoto(self):
        x = 1
        for imgurl in self.datas:
            urllib.urlretrieve(imgurl,'E://java/hei/%d.jpg'%x);
            x+=1;
        


