import matplotlib.pyplot as p

my_list_xvals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list_yvals = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# p.plot(my_list_xvals, my_list_yvals, linewidth=5)
# p.title("Square numbers", fontsize=24)
# p.xlabel("x", fontsize=14)
# p.ylabel("y", fontsize=14)
# p.show()

p.scatter(my_list_xvals, my_list_yvals, 50)
p.title("Square numbers", fontsize=24)
p.xlabel("x", fontsize=14)
p.ylabel("y", fontsize=14)
p.show()