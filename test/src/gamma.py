import matplotlib.pyplot as plt
x = ['0.7', '0.75', '0.8', '0.85', '0.9', '0.95', '1']
dis = 5412.214435
y = [0.2*1453.372299+dis*0.8-4620, 0.2*1455.183393+dis*0.8-4620, 0.2*1457.434984+dis*0.8-4620, 0.2*1459.272089+dis*0.8-4620,
     0.2*1460.295927+dis*0.8-4620, 0.2*1460.164068+dis*0.8-4620, 0.2*1458.507075+dis*0.8-4620]
plt.figure(figsize=(10, 5))
plt.title('the difference of γ effect on QoE', fontsize=20)
plt.xlabel(u'γ(decay rate)', fontsize=14)
plt.ylabel(u'QoE', fontsize=14)
plt.bar(x, y, color='#6CB7FF')
plt.savefig('./γ.svg')
plt.show()

