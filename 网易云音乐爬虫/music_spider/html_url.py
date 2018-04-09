class mange(object):
    def __init__(self):
        self.new_set = set()
        self.old_set = set()
    def add_new_url(self,url):
        if url not in self.new_set and url not in self.old_set:
            self.new_set.add(url)
        if url is None:
            return
    def has_url(self):
        return len(self.new_set)
    def get_url(self):
        new_url = self.new_set.pop()
        self.old_set.add(new_url)
        return new_url
    
    def add_new_urls(self,new_urls):
        for url in new_urls:
            self.new_set.add(url)
            