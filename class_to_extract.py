import csv

def extract():
    ratings_file = open("C:/Users/hp/Desktop/PROJECT/MOVIES DATASET/ratings.csv", "r")
    op_ratings_file = open("C:/Users/hp/Desktop/PROJECT/MOVIES DATASET/ratingsEx.csv", "w", newline = "")
    ip_read = csv.reader(ratings_file)
    op_write = csv.writer(op_ratings_file)

    for row in ip_read:
        size = len(row)
        op_row = ()
        op_row = (row[i] for i in range(size - 1))
        op_write.writerow(op_row)

    ratings_file.close()
    op_ratings_file.close()

extract()
            
