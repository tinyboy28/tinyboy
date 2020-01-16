import random

def get_mix_data():
  with open('weather_data.txt') as f:
    weather_data = f.readlines()
  with open('media.txt') as f:
    media_data = f.readlines()
  word_vocab = []
  pos_vocab = []
  target_vocab = []
  result = []
  for line in weather_data:
    word = []
    pos = []
    tag = []
    l = line.strip('\n').split('\t')
    words = l[0].split(' ')
    poss = l[1].split(' ')
    tags = l[2].split(' ')
    for i in range(len(poss)):
      for j in range(len(words[i])):
        pos.append(poss[i])
        tag.append(tags[i])
    tag.append('WEATHER')
    word = ' '.join(''.join(words))
    for ww in word:
      if ww not in word_vocab and ww != ' ':
        word_vocab.append(ww)
    for pp in pos:
      if pp not in pos_vocab:
        pos_vocab.append(pp)
    for tt in tag:
      if tt not in target_vocab:
        target_vocab.append(tt)
    pos = ' '.join(pos)
    tag = ' '.join(tag)

    result.append(word)
    result.append(pos)
    result.append(tag)
  # print(result)
  # print(len(result))

  words = media_data[::4]
  poss = media_data[1::4]
  tags = media_data[2::4]
  intents = media_data[3::4]

  index_list = []
  for i in range(len(words)):
    index_list.append(i)
  # for i in range(500):
  random.shuffle(index_list)
  for ind, i in enumerate(index_list):
    p = []
    t = []

    if ind > 500:
      break
    word = words[i].strip('\n').split(' ')
    pos = poss[i].strip('\n').split(' ')
    tag = tags[i].strip('\n').split(' ')
    intent = intents[i].strip('\n')
    for j in range(len(word)):
      for k in range(len(word[j])):
        p.append(pos[j])
        t.append(tag[j])
    t.append(intent)
    w = ' '.join(words[i].strip('\n').replace(' ', ''))
    for ww in w:
      if ww not in word_vocab and ww != ' ':
        word_vocab.append(ww)
    for pp in p:
      if pp not in pos_vocab:
        pos_vocab.append(pp)
    for tt in t:
      if tt not in target_vocab:
        target_vocab.append(tt)
    p = ' '.join(p)
    t = ' '.join(t)

    result.append(w)
    result.append(p)
    result.append(t)
    # print(w)
    # print(' '.join(p))
    # print(' '.join(t))
  # print(result)
  # print(word_vocab)
  # print(pos_vocab)
  # print(target_vocab)
  with open('word.vocab', 'w+') as f:
    f.write('\n'.join(word_vocab))
  with open('pos.vocab', 'w+') as f:
    f.write('\n'.join(pos_vocab))
  with open('target.vocab', 'w+') as f:
    f.write('\n'.join(target_vocab))

  with open('mix_data.txt', 'w+') as f:
    f.write('\n'.join(result))

get_mix_data()