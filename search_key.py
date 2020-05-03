import os

def search_key_name(dir, key):
  files = os.listdir(dir)
  res=[]
  for filename in files:
    if(filename.find(key)>=0):
      res.append(filename)
  return res

def search_key_content(dir, key):
  files = os.listdir(dir)
  res=[]
  for filename in files:
    if os.path.isfile(filename):
      f = open(filename)
      content = f.read()
      if(content.find(key)>=0):
        res.append(filename)
      f.close()
  return res

