from charm.toolbox.ecgroup import ECGroup, ZR, G
from charm.toolbox.eccurve import secp256k1
from charm.toolbox.hash_module import Hash
import hashlib

Hash_1 = hashlib.sha256
Hash_3 = hashlib.sha256

def system_setup(secp256k1):
    group = ECGroup(secp256k1)
    P = group.random(G)
    params = {'P': P, 'Group':group}
    return params

def server_keygen(params):
    group = ECGroup(secp256k1)
    s = group.random(ZR)
    SK_S = s
    PK_S = group.serialize(params['P']**s)
    return [SK_S, PK_S]

def user_keygen(params):
    a1, a2 = group.random(ZR), group.random(ZR) 
    SK_A = [group.serialize(a1), group.serialize(a2)]
    PK_A = [group.serialize(params['P']**a1), group.serialize(params['P']**a2)]
    
    b1, b2 = group.random(ZR), group.random(ZR)
    SK_B = [group.serialize(b1), group.serialize(b2)]
    PK_B = [group.serialize(params['P']**b1), group.serialize(params['P']**b2)]
    return [SK_A, PK_A, SK_B, PK_B]

def enc(params, kw, PK_S, SK_A, PK_B):
    PK_A_1, PK_A_2 = group.deserialize(PK_A[0]), group.deserialize(PK_A[1])
    SK_A_1, SK_A_2 = group.deserialize(SK_A[0]), group.deserialize(SK_A[1])
    PK_B_1, PK_B_2 = group.deserialize(PK_B[0]), group.deserialize(PK_B[1])
    PK_S = group.deserialize(PK_S)
    string_1 = group.serialize(PK_A_1).decode('utf-8') + group.serialize(PK_B_1).decode('utf-8') + group.serialize(PK_B_1**SK_A_1).decode('utf-8')
    lambda_1 = Hash_1(string_1.encode('utf-8')).hexdigest()
    string_2 = group.serialize(PK_A_2).decode('utf-8') + group.serialize(PK_B_2).decode('utf-8') + group.serialize(PK_B_2**SK_A_2).decode('utf-8')
    lambda_2 = Hash_1(string_2.encode('utf-8')).hexdigest()
    
    r = group.random(ZR)
    
    Q = (params['P']**r) ** group.hash((kw, lambda_1, lambda_2), ZR)
    C_1 = group.serialize(PK_S**r)
    C_2 = Hash_3(group.serialize(Q)).hexdigest()
    
    return [C_1, C_2]

def TrapGen(params, kw, PK_S, PK_A, SK_B):
    PK_A_1, PK_A_2 = group.deserialize(PK_A[0]), group.deserialize(PK_A[1])
    PK_B_1, PK_B_2 = group.deserialize(PK_B[0]), group.deserialize(PK_B[1])
    SK_B_1, SK_B_2 = group.deserialize(SK_B[0]), group.deserialize(SK_B[1])
    
    string_1 = group.serialize(PK_A_1).decode('utf-8') + group.serialize(PK_B_1).decode('utf-8') + group.serialize(PK_A_1**SK_B_1).decode('utf-8')
    lambda_1_ast = Hash_1(string_1.encode('utf-8')).hexdigest()
    string_2 = group.serialize(PK_A_2).decode('utf-8') + group.serialize(PK_B_2).decode('utf-8') + group.serialize(PK_A_2**SK_B_2).decode('utf-8')
    lambda_2_ast = Hash_1(string_2.encode('utf-8')).hexdigest()
    tr = group.serialize(group.hash((kw, lambda_1_ast, lambda_2_ast), ZR))
    return tr

def Test(SK_S, C, tr):
    c1 = group.deserialize(C[0])
    c2 = C[1]
    tr = group.deserialize(tr)
    temp = c1**tr
    Q_ast = temp**(SK_S**-1)
    return Hash_3(group.serialize(Q_ast)).hexdigest() == c2

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
    params = system_setup(secp256k1)
    group = ECGroup(secp256k1)
    [SK_S, PK_S] = server_keygen(params)
    [SK_A, PK_A, SK_B, PK_B] = user_keygen(params)
    c = enc(params, "keyword", PK_S, SK_A, PK_A, PK_B)
    tr = TrapGen(params, "keyword", PK_S, PK_A, SK_B)
    Test(SK_S, c, tr)