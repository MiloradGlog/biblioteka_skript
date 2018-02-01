import _mysql as mysql


db = mysql.connect("localhost", "root", "root", "skript_baza")


def popuniField():
    file = open("res/knjige.txt")
    red = file.readline()
    brojKnjige = 1;
    while red != "":

        redNiz = red.split('\x1e')
        print(redNiz)

        for f in redNiz:
           field = f[3:]
           fieldNumber = f[:3]
           query = """INSERT INTO field (fieldValue, bookNumber) VALUES ({},{})""".format(fieldNumber, brojKnjige)
           print(query)
           db.query(query)
        print("--------------------------")
        red = file.readline()
        brojKnjige += 1


def popuniSubField(field):
    p;

popuniField()