import csv

from mnn.csvtils.csvdata import csvdata

class csvreader:
  def __init__(self,file_name:str, delm=","):
    self.file_name = file_name
    self.delm = delm


  def read(self):
    data = csvdata()
    indexes = []
    with open(self.file_name, 'r', encoding='utf8') as csvfile:
      reader = csv.reader(csvfile,delimiter=self.delm)
      line_num = 0
      for row in reader:
        if line_num == 0:
          for name in row:
            indexes.append(name)
            data.add_index(name)
        else:
          for i,n in zip(indexes,row):
            data.add_data(i,n)
        line_num += 1
    return data