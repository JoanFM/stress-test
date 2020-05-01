import os

import numpy as np
from jina.drivers.helper import array2pb, pb2array
from jina.flow import Flow
from jina.proto import jina_pb2

GIF_BLOB = '/Volumes/TOSHIBA-4T/dataset/thumblr-gif-data/*.gif'  # 'data/*.gif'
replicas = 10

num_docs = 100
chunks_per_doc = 100
embed_dim = 1000

os.environ['JINA_ARRAY_QUANT'] = 'uint8'


def random_docs():
    c_id = 0
    np.random.seed(531)
    for j in range(num_docs):
        d = jina_pb2.Document()
        for k in range(chunks_per_doc):
            c = d.chunks.add()
            c.embedding.CopyFrom(array2pb(np.random.random([embed_dim])))
            c.chunk_id = c_id
            c.doc_id = j
            c_id += 1
        yield d


def get_output(req):
    np.random.seed(531)

    err = 0
    for d in req.docs:
        for c in d.chunks:
            recv = pb2array(c.embedding)
            send = np.random.random([embed_dim])
            err += np.sum(np.abs(recv - send)) / embed_dim

    print(f'reconstruction error: {err / num_docs:.6f}')


def f1():
    f = Flow(callback_on_body=True).add(yaml_path='_forward').add(yaml_path='_forward').add(yaml_path='_forward').add(
        yaml_path='_forward').add(yaml_path='_forward').add(yaml_path='_forward').add(yaml_path='_forward')
    with f as fl:
        fl.index(random_docs, callback=get_output, in_proto=True)


if __name__ == '__main__':
    f1()
