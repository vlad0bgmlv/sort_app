import tkinter as tk
import random


class SortingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sorting App")

        self.label = tk.Label(self.master, text="Select a sorting algorithm:")
        self.label.pack(pady=10)

        self.algorithms = ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort"]
        self.sort_var = tk.StringVar()
        self.sort_var.set(self.algorithms[0])

        self.sort_menu = tk.OptionMenu(self.master, self.sort_var, *self.algorithms)
        self.sort_menu.pack(pady=10)

        self.sort_button = tk.Button(self.master, text="Sort", command=self.sort_list)
        self.sort_button.pack(pady=10)\

        self.listbox = tk.Listbox(self.master)
        self.listbox.pack(pady=10)

        self.populate_list()

    def populate_list(self):
        self.listbox.delete(0, tk.END)
        for i in range(10):
            self.listbox.insert(tk.END, random.randint(1, 100))

    def sort_list(self):
        algorithm = self.sort_var.get()
        items = [int(self.listbox.get(i)) for i in range(self.listbox.size())]

        if algorithm == "Bubble Sort":
            items = bubble_sort(items)
        elif algorithm == "Selection Sort":
            items = selection_sort(items)
        elif algorithm == "Insertion Sort":
            items = insertion_sort(items)
        elif algorithm == "Merge Sort":
            items = merge_sort(items)

        self.listbox.delete(0, tk.END)
        for item in items:
            self.listbox.insert(tk.END, item)


def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items


def selection_sort(items):
    for i in range(len(items)):
        min_index = i
        for j in range(i+1, len(items)):
            if items[j] < items[min_index]:
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


def insertion_sort(items):
    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        while j >= 0 and key < items[j]:
            items[j+1] = items[j]
            j -= 1
        items[j+1] = key
    return items


def merge_sort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


root = tk.Tk()
app = SortingApp(root)
root.mainloop()