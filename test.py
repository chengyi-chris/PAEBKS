import matplotlib.pyplot as plt

number = [0,100,200,300,400,500,600,700,800,900,1000]
LL21 = [0.0, 0.17589831352233887, 0.3015289306640625, 0.43441224098205566, 0.5882828235626221, 0.7290325164794922, 0.8572192192077637, 1.003180980682373, 1.1446874141693115, 1.2890064716339111, 1.42093825340271]
ZQDT21 = [0.0, 0.16297101974487305, 0.29045987129211426, 0.4143991470336914, 0.6058926582336426, 0.7676105499267578, 0.8944399356842041, 1.0215320587158203, 1.1577274799346924, 1.3437557220458984, 1.4903783798217773]
Ours =[0.0, 0.18971824645996094, 0.31526732444763184, 0.438720703125, 0.5628657341003418, 0.7108113765716553, 0.8420493602752686, 0.9712047576904297, 1.128021478652954, 1.326528549194336, 1.4609708786010742]

plt.figure(figsize=(15,10),linewidth = 3)
plt.plot(number,LL21,'d-',color = 'g', markersize=25, linewidth=2,label="LL-PAEKS21")
plt.plot(number,ZQDT21,'*-',color = 'b',  markersize=25, linewidth=2,label="ZQDT-PEBKS21")
plt.plot(number,Ours,'X-',color = 'r', markersize=25, linewidth=2, label="Ours")

plt.xticks(fontsize=25)

plt.yticks(fontsize=25)

plt.xlabel("Number of Executions", fontsize=30, labelpad = 15)

plt.xlim([0,1000])
plt.ylim([0, 2])

plt.ylabel("Time Cost of Test (ms)", fontsize=30, labelpad = 20)


plt.legend(loc = "best", fontsize=25)

plt.savefig("test.png",dpi=600)
plt.show()