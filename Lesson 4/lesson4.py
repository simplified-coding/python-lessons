#Λίστες / List

#Λίστες είναι πιο σύνθετοι τύποι δεδομένων και περιέχουν μεταβλητές με συγκεκριμένη αρίθμηση.

#Σύνταξη

'''
<όνομα λίστας> = [<δεδομένα>, <δεδομένα>, <δεδομένα>]
'''

#Παράδηγμα

list_string=["Hello World"]

list_int=[1,2,3,5,7]

list_float=[6.14,9.63]

#Ιδιώτητες τις λίστας

'''
Η μεταβλητές στη λίστα ονομάζονται στοιχεία της λίστας και χωρίζονται μεταξύ τους με κόματα.
Η αρίθηση των στοιχείων ξεκινάει από το 0.
Μια λίστα μπορεί να λειτουργεί όπως κάθε μια μεταβλητή
'''

#Προσοχή όταν μέσα σε μία λίστα υπάρχουν χαρακτήρες δεν συμαίνει ότι δεν θα πρέπει να μπούν μέσα σε εισαγωγικά.

#Πως τυπώνουμε μια λίστα

list_numbers=[1,2,3,5,7,9,13,17]
print(list_numbers) #[1,2,3,5,7,9,13,17]
print(list_numbers[1]) #2
print(list_numbers[4]) #7
print(list_numbers[7]) #17

#Πως αλλάζουμε ένα στοιχείο της λίστας

'''
Ένα στοιχείο της λίστας μπορεί να αλλάξει όταν γράψουμε το στοιχείο (με βάση την αρίσμησή του) που θέλουμε να αλλάξει μεσα σε αγκύλες και μετά γράφουμε το στοιχείο με το οποίο θέλουμε αντικατασταθεί.
'''

#Σύνταξη 

'''
<όνομα λίστας> = [<δεδομένα>, <δεδομένα>, <δεδομένα>]
<όνομα λίστας>[<στοιχείο>] = [<νέο δεδομένο>]
'''''

#Παράδηγμα

list_numbers = [1,2,3,5,7,9,3,17]

list_numbers[7] = 19

# Για το extra μάθημα
date=[24,10,2022 , 26,10,2022]
print(date)
date[0]=25
date[3]=25
print(date)
date[-2]=9
date[-5]=9
print(date)

'''
Επίσης η Python μας δίνει την δυνατότητα να δημιουργήσουμε μία καινούρια λίστα αποκόβοντας ένα κομμάτι μίας προυπάρχουσας λίστας.Αυτό γίνετε με τούς εξής 4 τρόπους:

date[S:F]
date[S:]
date[:F]
date[:]

*S = Start / Αρχή   F = Finish / Τέλος 
'''