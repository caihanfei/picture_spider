class output(object):
    def __init__(self):
        self.datas = []
    def collect(self,data):
        if data is None:
            return
        self.datas.append(data)
    def file_output(self):
        file_gedan = open('/java/gedan.txt','w+')
        for data in self.datas:
            file_gedan.write(data.encode("utf-8"))
        file_gedan.close()