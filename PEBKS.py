from charm.toolbox.pairinggroup import PairingGroup,ZR,G1,G2,GT,pair
import hashlib

hash2 = hashlib.sha256

def setup(param_id='SS512'):
    group = PairingGroup(param_id)
    g = group.random(G1)
    h = group.random(G1)
    params = { 'g':g, 'h': h }
    return params

def keygen_r(params):
    alpha = group.random(ZR)
    sk_R = group.serialize(alpha)
    pk_R = group.serialize(params['g'] ** alpha)
    return [sk_R, pk_R]

def keygen_s(params):
    beta = group.random(ZR)
    sk_S = group.serialize(beta)
    pk_S = group.serialize(params['g'] ** beta)
    return [sk_S, pk_S]

def enc(pk_R, sk_S, kw, params):   
    sk_S = group.deserialize(sk_S)
    pk_R = group.deserialize(pk_R)
    r = group.random(ZR)
    k = pair(pk_R, params['h']) ** sk_S
    h1 = group.hash((k, kw), G1)

    A = params['g'] ** r
    t = pair(h1, A)
    B = hash2(group.serialize(t))
    return [group.serialize(A), B.hexdigest()]

def Trap_r(sk_R, pk_S, kw, params):
    sk_R = group.deserialize(sk_R)
    pk_S = group.deserialize(pk_S)
    k = pair(pk_S, params['h'])**sk_R
    h1 = group.hash((k, kw), G1)
    tr_R = group.serialize(h1)
    return tr_R

def Trap_s(sk_S, pk_R, kw, params):
    sk_S = group.deserialize(sk_S)
    pk_R = group.deserialize(pk_R)
    k = pair(pk_R, params['h'])**sk_S
    h1 = group.hash((k, kw), G1)
    tr_S = group.serialize(h1)
    return tr_S

def Test(td, c):
    A = group.deserialize(c[0])
    B = c[1]
    td = group.deserialize(td)
    return hash2(group.serialize(pair(td, A))).hexdigest() == B

def cal_time():
    list_time = []
    temp = 0
    start = time.time()
    for i in range(1,1001):
        ## insert which calculation you want
    end = time.time()
    temp += end - start
    list_time.append(temp)
    print(list_time)
    
if __name__ == '__main__':
    param_id = 'SS512'
    params = setup(param_id)
    group = PairingGroup(param_id)
    [sk_R, pk_R] = keygen_r(params)
    [sk_S, pk_S] = keygen_s(params)

    c = enc(pk_R, sk_S, "keyword", params)
    td_r = Trap_r(sk_R, pk_S, "keyword", params)
    Test(td_r, c)
