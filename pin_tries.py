MAX_TRIES = 3
CORRECT_PIN = "2580"
tries = 0
while tries < MAX_TRIES :
    PIN = input ("PIN :")
    if PIN == CORRECT_PIN :
     print (f"Access granted.")
     break
    else :
     tries += 1
     print (f"Wrong PIN. Tries left:{MAX_TRIES - tries}.")
    if tries == MAX_TRIES :
     print ("Card blocked.")
