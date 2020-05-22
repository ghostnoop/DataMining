import matplotlib as mpl
import matplotlib.pyplot as plt


def graph4_0(datas):
    data_names = []
    data_values = []
    for i in datas:
        data_names.append(i.name)
        data_values.append(i.count)

    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(900 / dpi, 600 / dpi))
    mpl.rcParams.update({'font.size': 11})

    plt.title('The best products')

    ax = plt.axes()
    ax.yaxis.grid(True, zorder=1)

    xs = range(len(data_names))

    plt.bar([x for x in xs], [d * 1 for d in data_values],
            width=0.2, color='red', alpha=0.7,
            zorder=2)

    plt.xticks(xs, data_names)

    fig.autofmt_xdate(rotation=90)

    plt.legend(loc='upper right')
    fig.savefig('graph.png')
