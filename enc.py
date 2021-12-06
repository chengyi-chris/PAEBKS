import matplotlib.pyplot as plt

number = [0,100,200,300,400,500,600,700,800,900,1000]
ZQDT21 = [0.0, 0.9811453819274902, 1.9186437129974365, 2.765719175338745, 3.6402041912078857, 4.478187322616577, 5.441918849945068, 6.28490948677063, 7.145695686340332, 7.982342004776001, 8.815263032913208]
LL21 = [0.0, 0.39853835105895996, 0.7231905460357666, 1.124175786972046, 1.464216947555542, 1.799316644668579, 2.123908042907715, 2.470299005508423, 2.803544759750366, 3.1328699588775635, 3.4621214866638184]
Ours = [0.0, 0.34710168838500977, 0.7035367488861084, 1.0655503273010254, 1.4267995357513428, 1.7706208229064941, 2.11557936668396, 2.4594383239746094, 2.776275873184204, 3.1370766162872314, 3.5402073860168457]

plt.figure(figsize=(15,10),linewidth = 3)
plt.plot(number,LL21,'d-',color = 'g', markersize=25, linewidth=2,label="LL-PAEKS21")
plt.plot(number,ZQDT21,'*-',color = 'b',  markersize=25, linewidth=2,label="ZQDT-PEBKS21")
plt.plot(number,Ours,'X-',color = 'r', markersize=25, linewidth=2, label="Ours")
         
plt.xticks(fontsize=30)

plt.yticks(fontsize=30)

plt.xlabel("Number of Executions", fontsize=30, labelpad = 15)

plt.xlim([0, 1000])
plt.ylim([0, 10])

plt.ylabel("Time Cost of Keyword Encryption (ms)", fontsize=30, labelpad = 20)


plt.legend(loc = "best", fontsize=25)

plt.savefig("enc.png",dpi=600)
plt.show()