import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{name}.png')
  plt.close()
  #plt.show()

def generate_pie_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig(f'./imgs/{name}.png')
  plt.close()
  #plt.show()


def generate_plot_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.plot(labels, values, linewidth=2.0)
  plt.savefig(f'./plot/{name}.png')
  plt.close()
  #plt.show()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)