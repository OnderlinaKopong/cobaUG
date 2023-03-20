class Browser:
    def _init_(self):
        self.history = [] 
        self.current = -1 
    def go(self, url):
        while len(self.history) > self.current+1:
            self.history.pop()
        self.history.append(url) 
        self.current += 1 
    def back(self):
        if self.current > 0:
            self.current -= 1 
            return self.history[self.current] 
        return None 
    def forward(self):
        if self.current < len(self.history)-1:
            self.current += 1 
            return self.history[self.current] 
        return None 
    def printAll(self):
        for url in self.history:
            print(url)


browser = Browser()

browser.go("https://google.com")
browser.go("https://ukdw.ac.id")
browser.go("https://facebook.com")

print(browser.back()) # output: https://ukdw.ac.id
print(browser.back()) # output: https://google.com
print(browser.forward()) # output: https://ukdw.ac.id

browser.go("https://twitter.com")
browser.printAll() # output: https://google.com https://ukdw.ac.id https://twitter.com