import matplotlib
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
plt.rcParams['font.sans-serif']=['SimHei']
x = np.arange(3)
model_accuracy = [87, 97, 99]
bars = ax.bar(x, model_accuracy, width=0.3, label="准确率(%)")

ax.set_title(u'模型准确率对比')
ax.set_xticks(x)
ax.set_xticklabels(('NB', 'ANN', 'CNN'))
ax.legend()
for barA in bars:
    ax.text(barA.get_x()+barA.get_width()/2, barA.get_height(), '%d' % int(barA.get_height()), ha='center', va='bottom')
fig.tight_layout()
plt.show()