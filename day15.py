import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
#Generate sample health metrics dataset
num_weeks=10
individuals=['Person1','Person2','Person3']
metrics=['Body Weight','Body Temperatures','Sleep Duration']
sample_data={
    individual: {metric:np.random.uniform(50,100,num_weeks)
                if metric=='Body weight'
                else np.random.uniform(36.0,37.5,num_weeks)
                if metric=='Body Temperature'
                else np.random.uniform(5,10,num_weeks)
                for metric in metrics}
    for individual in individuals
}

def plot_metrics(individual_name,metric_name,visualization_type):
    values=sample_data.get(individual_name,{}).get(metric_name,[])
    x_values=range(1,len(values)+1)
    plt.figure(figsize=(6,4))
    if visualization_type=='Line Plot':
        plt.plot(x_values,values,marker='o')
    elif visualization_type=='Bar Chart':
        plt.bar(x_values,values)
    plt.title(f'{metric_name}of{individual_name}')
    plt.xlabel('Week')
    plt.ylabel(metric_name)
    plt.xticks(x_values)
    plt.show()

def visualize_data():
    selected_individual=individual_combobox.get()
    selected_metric=metric_combobox.get()
    selected_visualization=visualization_combobox.get()

    if selected_individual and selected_metric and selected_visualization:
        plot_metrics(selected_individual,selected_metric,selected_visualization)


#GUI Setup
root=tk.Tk()
root.title('Health Metrics Visualization')

#Individual selection dropdown
individual_label=ttk.Label(root, text='Select Individual:')
individual_label.pack()

individual_combobox=ttk.Combobox(root, values=individuals)
individual_combobox.pack()
#Metric selection dropdown
metric_label=ttk.Label(root,text='Select Metric:')
metric_label.pack()
metric_combobox=ttk.Combobox(root,values=metrics)
metric_combobox.pack()
#visualization selection dropdown
visualization_label=ttk.Label(root,text='Select Visualization:')
visualization_label.pack()
visualization_combobox=ttk.Combobox(root,values=['Line Plot','Bar Chart'])
visualization_combobox.pack()
#Visualization buttons
visualize_button=ttk.Button(root,text='Visualize Metrics',command=visualize_data)
visualize_button.pack()
exit_button=ttk.Button(root,text='Exit',command=root.destroy)
exit_button.pack()
root.mainloop()