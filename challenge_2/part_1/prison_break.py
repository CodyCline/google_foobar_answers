'''
| 7
| 4 8
| 2 5 9
| 1 3 6 10

Example Google gave me
'''
def solution(x, y):
    cell_number = 0 
    x_count = 0 
    while x_count < x: 
        x_count += 1 
        cell_number += x_count
        if x_count == x: #If equal to x_count
            y_count = 1 
            y_increment = x_count #Copy the current x_count and then iterate
            while y_count < y: 
                y_count += 1
                cell_number += y_increment
                y_increment += 1
            return(str(cell_number))

print(solution(5, 10))