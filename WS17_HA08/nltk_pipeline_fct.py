# TODO - use PENN Treebank word types

import nltk
Lemmatizer = nltk.stem.WordNetLemmatizer()

""" Read a file by filename its contents """
def read_file(filename):
  with open(filename) as active_file:
    return active_file.read()

""" Write lines to a file """
def write_file(filename, lines):
  with open(filename, 'w') as active_file:
    for line in lines:
      active_file.write(line)

def render_line(token_tuple):
  return token_tuple


""" Take a sentence as string. Return array of (original_word, lemmatized, POS) """
def process_sentence(sent):
  tokenized = nltk.word_tokenize(sent, language='english', preserve_line=False)
  tagged = nltk.pos_tag(tokenized, tagset=None, lang='eng')
  return list(map(lemmatize_word, tagged))

POS_MAP = {
  'N': 'n',
  'V': 'v',
  'J': 'a',
  'R': 'r',
  'S': 's'
}

def get_wn_pos_constant(pos):
  try:
    constant = POS_MAP[pos[0:1]]
  except KeyError:
    constant = POS_MAP['S']
  return constant


def lemmatize_word(word_tuple):
  pos = get_wn_pos_constant(word_tuple[1])
  lemma = Lemmatizer.lemmatize(word_tuple[0], pos='n')
  return (word_tuple[0], lemma, word_tuple[1])

def annotate_corpus_with_nltk_pipeline(input_filename, language):
  text = read_file(input_filename)
  sentences = nltk.sent_tokenize(text, language='english')
  annotated_sentences = list(map(process_sentence, sentences))
  return annotated_sentences

def flatten_and_render(sentences):
  lines = []
  for si, sent in enumerate(sentences):
    for wi, word in enumerate(sent):
      line = str(si) + '\t' + str(wi) + '\t' + str(word[0]) + '\t' + str(word[1]) + '\t' + str(word[2]) + '\n'
      print(line)
      lines.append(line)
  return lines

def write_conll_format_output(output_filename, sentences):
  lines = flatten_and_render(sentences)
  write_file(output_filename, lines)
