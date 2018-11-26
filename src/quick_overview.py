import json
PATH = '../data/bytecup.corpus.train.0.txt'

with open(PATH) as f:
    line = f.readline()  # line is <class 'str'>
    d = json.loads(line)  # d is <class 'dict'>
    print(type(f),type(line),type(d),d.keys())
    print(d['content'])
    print(d['id'])
    print(d['title'])

    lines = f.readlines()
    print(len(lines),type(lines))  # lines is <class 'list'>


PATH_VAL = '../data/bytecup.corpus.validation_set.txt'
with open(PATH_VAL) as f:
    line = f.readline()  # line is <class 'str'>
    d = json.loads(line)  # d is <class 'dict'>
    print(type(f),type(line),type(d),d.keys())
    print(d['content'])
    print(d['id'])

    lines = f.readlines()
    print(len(lines),type(lines))  # lines is <class 'list'>
