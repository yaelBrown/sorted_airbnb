class ResultsModel: 
  def __init__(self, photo = None, title = None, sTitle = None, amenities = None, rating = None, price = None):
    self.photo = photo
    self.title = title
    self.sTitle = sTitle
    self.amenities = amenities
    self.rating = rating
    self.price = price

  def serialize(self):
    return {
      "photo": self.photo,
      "title": self.title,
      "sTitle": self.sTitle,
      "amenities": self.amenities,
      "rating": self.rating,
      "price": self.price
    }






if __name__ == "__main__":

  test = ResultsModel("photo", "title", "stitle", "amenitiez", "rating", "price")
  print(test.serialize())

  