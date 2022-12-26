# Dictionaries

'''
Τα λεξικά είναι τύποι δεδoμένων που μας επιτρέπουν μια προσεγμένη αποθήκευση δεδομένων
σε μορφή που θυμίζει λεξικό ή και ευρητήριο
'''

# Σύνταξη

'''
<όνομα λεξικού> = {"κλειδή": "τιμή", "κλειδή": "τιμή", "κλειδή": "τιμή"}

Μπορούμε να σκεφτούμε τα κλειδιά ως λέξεις στο λεξικό μας
και τις τιμές ως τις ερμηνίες των κλειδιών

'''

# Παράδηγμα

my_dog = {"name": "Ermis", "age": 1}

# Ιδιότητες

'''
- Μπορούμε να ορίσουμε κλειδιά και τιμές σε οποιονδήποτε τύπο δεδομένου
πχ: Αριθμός, Χαρακτήρας, κτλ.

- Μπορούμε κι όλας να ορίσουμε τιμές ως λίστες!

- Κλειδιά και τιμές μπορούν να είναι διαφορετικός τύπος δεδομένου.
'''

# Επεκτηνόμενα λεξικά

'''
Μπορούμε να επεκτήνουμε λεξικά με πολλά δεδομένα για να είναι πιο ευανάγνωστα.
'''

# Σύνταξη 

'''
<όνομα λεξικού> = {
    "κλειδή": "τιμή",
    "κλειδή": "τιμή"
}
'''

# Παράδηγμα

my_dog = {

    "name": "Ermis",
    "age": 1

}

# Αλλαγή τιμής λεξικού

# Σύνταξη

'''
<όνομα λεξικού>[<κλειδή>*] = <νέα τιμή κλειδιού>

* Αν το κλειδή είναι χαρακτήρας πρέπει να μπουν ""
'''

# Παράδηγμα

my_dog["age"] = 3

# Χρήση λεξικού

'''
Μπορούμε να χρησιμοποιοίσουμε ένα λεξικό (σε ένα print() για παράδηγμα) όπως με τις λίστες
'''

# Παράδηγμα

print(my_dog)
print(my_dog["age"])