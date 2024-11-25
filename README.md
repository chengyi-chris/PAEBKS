# [PAEBKS](https://www.sciencedirect.com/science/article/abs/pii/S1383762122001631)

This is an official implementation of PAEBKS proposed by our paper "[Privacy-preserving bidirectional keyword search over encrypted data for cloud-assisted IIoT](https://www.sciencedirect.com/science/article/abs/pii/S1383762122001631)". 

## Abstact
Cloud-assisted industrial Internet of Things (IIoT) technology is increasingly used by related enterprises. To preserve the privacy of sensitive data, IIoT devices must encrypt data before sending them to a cloud server. Public-key encryption with keyword search (PEKS) provides an important search function over cloud-assisted IIoT, allowing users to search for encrypted data without decryption. To increase practical functionality, Zhang et al. recently proposed the concept of public-key encryption with bidirectional keyword search, which supports both sender and receiver searches. However, their scheme provides insufficient security because it cannot resist keyword guessing attacks (KGA). Additionally, their scheme requires time-consuming bilinear pairing operations, resulting in high computational costs. In this study, a novel concept called public-key authenticated encryption with bidirectional keyword search was devised for multi-user settings. The system definition and security requirements are formally defined to ensure that no adversary can overcome the indistinguishability against chosen-keyword attacks or KGA. Furthermore, we propose a pairing-free semi-generic construction, combining a multiparty non-interactive protocol and authenticated functionality, which has proven to be secure under the standard model. The experimental results reveal that, compared with other state-of-the-art schemes, the proposed scheme is more practical, secure, and suitable for use with cloud-assisted IIoT systems.

## Details of implementation
This project provides PoC implementations to evaluate the performance of the following schemes:

1. Our scheme - Journal of Systems Architecture - [Public-key authenticated encryption with bidirectional keyword search (PAEBKS)](https://www.sciencedirect.com/science/article/abs/pii/S1383762122001631)
2. ZWDT21 - Computer Standards & Interfaces - [Public-key encryption with bidirectional keyword search and its application to encrypted emails.](https://doi.org/10.1016/j.csi.2021.103542) 
3. LL21 - IEEE Trans. Mobile Computing - [Lightweight Public Key Authenticated Encryption with Keyword Search against Adaptively-Chosen-Targets Adversaries for Mobile Devices.](https://doi.org/10.1109/TII.2020.3006474)

For the bilinear-pairing scheme (ZWDT21), we implement them by using PBC library with Type-A pairing (160, 512) for 80-bit security. For a pairing-free scheme (LL21), we implement it by using Charm library with parameter spec160r1 for 80-bit security.

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

