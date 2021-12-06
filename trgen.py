import matplotlib.pyplot as plt

number = [0,100,200,300,400,500,600,700,800,900,1000]

LL21 = [0.0, 0.20100975036621094, 0.34860920906066895, 0.48934173583984375, 0.6630880832672119, 0.8151407241821289, 0.9526145458221436, 1.0926334857940674, 1.2399260997772217, 1.3932158946990967, 1.5305814743041992]
ZQDT21 = [0.0, 0.5913481712341309, 1.1227843761444092, 1.6678109169006348, 2.195315361022949, 2.7435648441314697, 3.306457996368408, 3.8488965034484863, 4.46084189414978, 5.031727313995361, 5.57181715965271]
Ours = [0.0, 0.18838262557983398, 0.3274853229522705, 0.4670133590698242, 0.6423931121826172, 0.778287410736084, 0.9336011409759521, 1.0851657390594482, 1.2383122444152832, 1.3747966289520264, 1.5087261199951172]

plt.figure(figsize=(15,10),linewidth = 3)
plt.plot(number,LL21,'d-',color = 'g', markersize=25, linewidth=2,label="LL-PAEKS21")
plt.plot(number,ZQDT21,'*-',color = 'b',  markersize=25, linewidth=2,label="ZQDT-PEBKS21")
plt.plot(number,Ours,'X-',color = 'r', markersize=25, linewidth=2, label="Ours")

plt.xticks(fontsize=25)

plt.yticks(fontsize=25)

plt.xlabel("Number of Executions", fontsize=30, labelpad = 15)

plt.xlim([0,1000])
plt.ylim([0, 7])

plt.ylabel("Time Cost of Trapdoor Generation (ms)", fontsize=30, labelpad = 20)

plt.legend(loc = "best", fontsize=25)

plt.savefig("trgen.png",dpi=600)
plt.show()