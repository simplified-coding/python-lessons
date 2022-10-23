#Ισοδυναμίες

'''
== | Ίσο
!= | Δεν είναι ίσο
>= | Μεγαλύτερο ή ίσο
<= | Μικρότερο ή ίσο
>  | Μεγαλύτερο
<  | Μικρότερο
'''

#If / Εάν

#Σύνταξη

'''
if <προϋπόθεση>:
	<αποτέλεσμα>
'''

#Εάν η προϋπόθεση ισχύει, τότε το αποτέλεσμα τρέξει

#Παράδειγμα

example = True

if example == True:
	print("hello")

#Εάν η προϋπόθεση δεν ισχύει, τότε το αποτέλεσμα δεν πραματοποιήται

#Παράδειγμα

example = False

if example == True:
	print("hello")

#Εlif

#Εάν η προϋπόθεση ισχύει, τότε μπορούμε να ελέγχουμε αν μια άλλη θα πραγματοποιηθεί

#Παράδειγμα

example = True

if example == True:
	print("hello")

elif example == False:
	print("hello again")

#Προσοχή! Το elif πρέπει να είναι ακριβός από κάτω ένα άλλο if ή elif

#Εlse

#Στην περίπτωση που καμία από τις προηγούμενες προϋπόθεσεις δεν ισχύσει, τότε το else θα πραγματοποιηθεί.

#Παράδειγμα

example = 0

if example == True:
	print("Hello!!")

elif example == False:
	print("Hello!")
	
else:
	print("Hello")

number = 5

if number >= 6:
	print("Είναι μεγαλύτερο από 6")

elif number <= 4:
	print("Είναι μικρότερο από 4")

elif number != 5:
	print("Δεν είναι 5")

elif number == 5:
	print("Είναι 5")