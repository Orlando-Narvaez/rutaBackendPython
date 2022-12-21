import matplotlib.pyplot as plt

def generateBarChart(labels,values): #Grafica de barras
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.show()

def generatePieChart(labels,values): #Grafica de pastel
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis("equal")
    plt.show()

if __name__  == "__main__":
    labels = ["a", "b", "c"]
    values = [100, 200, 80]
    #generateBarChart(labels,values)
    generatePieChart(labels,values)