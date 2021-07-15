class Repository:
  def __init__(self, cnx):
    self.cnx = cnx

  def execute(self, query, params=None):
    self.cursor = self.cnx.cursor()
    self.cursor.execute(query, params)

    return self
    
  def commit(self):
    self.cnx.commit()

    return self
    
  def transform(self, columns, row):
    result = {}
    for key, value in zip(columns, row):
      result[key] = value

    return result
  
  def to_item(self, columns):
    row = self.cursor.fetchone()
    self.cursor.close()

    return self.transform(columns, row)
  
  def to_list(self, columns):
    result = []
    for row in self.cursor:
      item = self.transform(columns, row)
      result.append(item)
    
    self.cursor.close()

    return result