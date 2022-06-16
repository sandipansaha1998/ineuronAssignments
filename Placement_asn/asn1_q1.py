class Assignment1:
  def __init__(self):
    pass
  def replace(self,sen,word1,word2):
    sen = sen+' '
    new_sen=''
    word=''
    for l in sen:
        if l == ' ':
            if word == word1:
                word = word2
            new_sen = new_sen+' '+word
            word = ''
        else:
            word = word+l
    return new_sen
  def task(self):
    file_obj = open('example.txt','w+')
    file_obj.write('this is a placement assignment')
    file_obj.close()
    file_obj = open('example.txt','r+')
    sentence = file_obj.read()
    file_obj.close()
    new_sentence = self.replace(sentence,'placement','screening')
    file_obj = open('example.txt','w')
    file_obj.write(new_sentence)
    file_obj.close()

if __name__ == "__main__":
    Assignment1().task()
    print("Success")
    
    