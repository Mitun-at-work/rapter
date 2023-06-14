import os


class RaptorPDF :
    def __init__(self) -> None:
        self.directoryLink = f"{os.curdir}/reports"
        


"""
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# generate a list with dummy plots   
figs = []
for i in [-1, 1]:
    fig = plt.figure()
    plt.plot([1, 2, 3], [i*1, i*2, i*3])
    figs.append(fig)

# gerate a multipage pdf:
with PdfPages('multipage_pdf.pdf') as pdf:
    for fig in figs:
        pdf.savefig(fig)
        plt.close()
"""




        
    