from word_segmentor import SentenceSplit_pb2, SentenceSplit_pb2_grpc
import grpc

segmentor_params = SentenceSplit_pb2.SplitParams()
segmentor_params.keep_punc = True
segmentor_params.need_pos = True
segmentor_params.rec_long_entity = True
segmentor_params.rec_ambiguous_entity = True
segmentor_params.auto_rec_nr = True
segmentor_params.recognizer_entity = True
segmentor_params.need_term_weight = False

# segmentor_channel = grpc.insecure_channel('10.110.30.107:9000')
# segmentor_channel = grpc.insecure_channel('10.153.127.85:9000')
segmentor_channel = grpc.insecure_channel('10.19.28.67:9000')
segmentor_stub = SentenceSplit_pb2_grpc.sendStub(segmentor_channel)

def word_segment(sentence):
    request = SentenceSplit_pb2.splitRequest(text=sentence, params=segmentor_params)
    r = segmentor_stub.split(request)
    return r.word, r.pos

def process_bert_data():
    name_array = ['train', 'test', 'dev']

    with open('train/seq.in') as f:
        lines_train = f.readlines()
    with open('test/seq.in') as f:
        lines_test = f.readlines()
    with open('valid/seq.in') as f:
        lines_valid = f.readlines()

    lines_all = []
    lines_all.append(lines_train)
    lines_all.append(lines_test)
    lines_all.append(lines_valid)

    pos_library = []
    word_library = []

    pos_library.append('<s>')
    pos_library.append('</s>')
    pos_library.append('<unk>')

    word_library.append('<s>')
    word_library.append('</s>')
    word_library.append('<unk>')

    for ind in range(3):
        pos = []
        jj = 0
        for line in lines_all[ind]:
            for li in line.strip('\n').split(' '):
                if li not in word_library:
                    word_library.append(li)


            ws, ps = word_segment(''.join(line.strip('\n').split(' ')))
            p_temp = []

            for i, w in enumerate(ws):
                if ps[i] not in pos_library:
                    pos_library.append(ps[i])
                for j in range(len(w)):
                    p_temp.append(ps[i])
            pos.append(' '.join(p_temp))
            jj += 1
            print(jj)
        result = []
        with open('{}.in'.format(name_array[ind])) as f:
            tag = f.readlines()
        for i, line in enumerate(lines_all[ind]):
            print(i)
            result.append(line)
            result.append(pos[i])
            result.append('\n')
            result.append(tag[i])
        with open('{}.in'.format(name_array[ind]), 'w+') as f:
            f.write(''.join(result))


    with open('word.vocab', 'w+') as f:
        f.write('\n'.join(word_library))
    with open('target.vocab', 'w+') as f:
        f.write('\n'.join(pos_library))



# def process

process_bert_data()
# process_bert_data('test')
# process_bert_data('dev')
