# Stress Test

A collection of stress tests of Jina infrastructure


## Case 1: Slow Worker for Testing Load Balancing

To test `--scheduling`

[slow_worker](slow_worker/app.py)


## Case 2: IO Bounded Worker

To test `--prefetch` and `--prefetch-size`

[io_bound](io_bound/app.py)

## Case 3: Quantization 

To test `JINA_ARRAY_QUANT` unset, `fp16` and `uint8`

[io_bound](io_bound/app.py)
