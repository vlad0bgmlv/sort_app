import tkinter as tk
# from tkinter import simpledialog
from tkinter import messagebox
# import random
from MergeSort import merge_sort
from SelectionSort import selection_sort
from InsertionSort import insertion_sort
from BubbleSort import bubble_sort


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
        self.sort_button.pack(pady=10)

        self.listbox = tk.Listbox(self.master)
        self.listbox.pack(pady=10)

        self.populate_list_button = tk.Button(self.master, text="Populate List", command=self.populate_list)
        self.populate_list_button.pack(pady=10)

    # def populate_list(self):
    #     self.listbox.delete(0, tk.END)
    #     num_items = simpledialog.askinteger("Input", "How many items would you like to insert?")
    #     if num_items is not None:
    #         for i in range(num_items):
    #             item = simpledialog.askinteger("Input", f"Enter item {i+1}:")
    #             if item is not None:
    #                 self.listbox.insert(tk.END, item)

    def populate_list(self):
        self.listbox.delete(0, tk.END)
        input_window = tk.Toplevel(self.master)
        input_window.title("Enter Values")
        input_window.geometry("200x200")

        input_label = tk.Label(input_window, text="Enter the length of the array:")
        input_label.pack(pady=10)

        input_entry = tk.Entry(input_window)
        input_entry.pack(pady=10)

        submit_button = tk.Button(input_window, text="Submit",
                                  command=lambda: self.get_values(input_entry.get(), input_window))
        submit_button.pack()

    def get_values(self, length, input_window):
        try:
            length = int(length)
            input_window.destroy()
            input_window = tk.Toplevel(self.master)
            input_window.title("Enter Values")
            input_window.geometry("200x200")

            input_label = tk.Label(input_window, text=f"Enter {length} values (separated by spaces):")
            input_label.pack(pady=10)

            input_entry = tk.Entry(input_window)
            input_entry.pack(pady=10)

            submit_button = tk.Button(input_window, text="Submit", command=lambda: self.update_list(input_entry.get()))
            submit_button.pack()
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid integer for the length of the array.")

    def update_list(self, values):
        try:
            items = [int(val) for val in values.split()]
            for item in items:
                self.listbox.insert(tk.END, item)
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter valid integer values separated by spaces.")

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


# def bubble_sort(items):
#     for i in range(len(items)):
#         for j in range(len(items) - 1):
#             if items[j] > items[j+1]:
#                 items[j], items[j+1] = items[j+1], items[j]
#     return items


# def selection_sort(items):
#     for i in range(len(items)):
#         min_index = i
#         for j in range(i+1, len(items)):
#             if items[j] < items[min_index]:
#                 min_index = j
#         items[i], items[min_index] = items[min_index], items[i]
#     return items


# def insertion_sort(items):
#     for i in range(1, len(items)):
#         key = items[i]
#         j = i - 1
#         while j >= 0 and key < items[j]:
#             items[j+1] = items[j]
#             j -= 1
#         items[j+1] = key
#     return items


# def merge_sort(items):
#     if len(items) <= 1:
#         return items
#
#     mid = len(items) // 2
#     left = items[:mid]
#     right = items[mid:]
#
#     left = merge_sort(left)
#     right = merge_sort(right)
#
#     return merge(left, right)
#
#
# def merge(left, right):
#     result = []
#     i, j = 0, 0
#
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     result += left[i:]
#     result += right[j:]
#
#     return result


root = tk.Tk()
app = SortingApp(root)
root.mainloop()
