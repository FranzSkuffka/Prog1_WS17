from shared import lemmatize

class Word:
  """ Supports lemmatizing """
  def set_tag(self, tag):
    self.tag = tag

  def lemmatize(self):
    self.lemma = lemmatize(self.text, self.tag)

  def render(self):
    return str(self.text) + '\t' + str(self.lemma) + '\t' + str(self.tag)


  def __init__(self, text):
    self.text = text
    self.tag = None
    self.lemma = None
