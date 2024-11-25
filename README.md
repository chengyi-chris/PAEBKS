# [PAEBKS](https://www.sciencedirect.com/science/article/abs/pii/S1383762122001631)

This is an official implementation of PAEBKS proposed by our paper "[Privacy-preserving bidirectional keyword search over encrypted data for cloud-assisted IIoT](https://www.sciencedirect.com/science/article/abs/pii/S1383762122001631)". 

This project provides PoC implementations to evaluate the performance of the following schemes, which adopt the PBC library with Type-A pairing (160, 512) for 80-bit security.

- Our scheme: Hierarchical identity-based puncturable inner product functional encryption (HIBP-IPFE)
- SDH+21's work: [Hierarchical identity-based inner product functional encryption](https://doi.org/10.1016/j.ins.2021.05.062)

This project provides PoC implementations to evaluate the performance of the following schemes:

1. ZWDT21 - Computer Standards & Interfaces - [Public-key encryption with bidirectional keyword search and its application to encrypted emails.](https://doi.org/10.1016/j.csi.2021.103542) 
2. LL21 - IEEE Trans. Mobile Computing - [Lightweight Public Key Authenticated Encryption with Keyword Search against Adaptively-Chosen-Targets Adversaries for Mobile Devices.](https://doi.org/10.1109/TII.2020.3006474)

The code implementation of Public key authenticated bidirectional keyword search

For the bilinear-pairing scheme (ZWDT21), we implement them by using PBC library with Type-A pairing (160, 512) for 80-bit security.

For a pairing-free scheme (LL21), we implement it by using Charm library with parameter spec160r1 for 80-bit security.

## Required library

- [GMP 5.x](http://gmplib.org/)
- [PBC](http://crypto.stanford.edu/pbc/news.html)
- [OPENSSL](http://www.openssl.org/)
- [Charm-crypto](https://jhuisi.github.io/charm/install_source.html)

## Perform code

1. For bilinear-pairing scheme (ZWQT21):

   ```
   python3 PEBKS.py
   ```

2. For pairing-free scheme (LL21):

   ```
   python3 PAEKS.py
   ```

3. For our PAEBKS scheme:

   ```
   python3 PAEBKS.py
   ```

To execute the cost of scheme 1000 times: we add `cal_time() ` in each scheme, you can perform which operations or algorithms for simple tests.

## Test performance

To generate the performance for each algorithm, we provide the result code in the below folder.

```
## For encryption algorithm
python3 enc.py

## For trapdoor algorithm
python3 trgen.py

## For testing algorithm
python3 test.py
```

## Results

 

| Encrypt keywords  | Generate trapdoors    | Test                |
| ----------------- | --------------------- | ------------------- |
| ![enc](./enc.png) | ![trgen](./trgen.png) | ![test](./test.png) |

