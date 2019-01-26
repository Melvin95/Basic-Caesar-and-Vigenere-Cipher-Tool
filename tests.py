import caesar_cipher as CAESAR
import vigenere_cipher as VIGENERE
import common

'''
CAESAR CIPHER TESTS
'''
print("***CAESAR ENCRYPTION***")
print(CAESAR.encrypt("a",26*1222)=="a")
print(CAESAR.encrypt("a",27)=="b")
print(CAESAR.encrypt("a",25)=="z")
print(CAESAR.encrypt("z",25)=="y")
print(CAESAR.encrypt("z",27)=="a")
print(CAESAR.encrypt("a",26*26)=="a")
print(CAESAR.encrypt("a",27*27)=="b")
print(CAESAR.encrypt("a",25)=="z")
print(CAESAR.encrypt("a",625)=="b")
print(CAESAR.encrypt("z",27*3)=="c")
print("\n***CAESAR DECRYPTION***")
print(CAESAR.decrypt("a",26*1222)=="a")
print(CAESAR.decrypt("b",27)=="a")
print(CAESAR.decrypt("z",25)=="a")
print(CAESAR.decrypt("y",25)=="z")
print(CAESAR.decrypt("a",27)=="z")
print(CAESAR.decrypt("a",26*26)=="a")
print(CAESAR.decrypt("b",27*27)=="a")
print(CAESAR.decrypt("z",25)=="a")
print(CAESAR.decrypt("b",625)=="a")
print(CAESAR.decrypt("c",27*3)=="z")
print("\n***VIGENERE DECRYPTION***")
print(VIGENERE.decrypt("DM FR QS XU CF DM MZSY M BRUHK MFSY XU CF DM FR QS XU JRMDZ ZY SXF UFQ XIEL DM FR QS XU CF DM MDZJR UCTFS QZYZ YY CF DM FR QS XU CF KUGGQW MM TFF NY EJPF NZRW KILWW RYVQAZA SQMQ DLXL XYK F KYCCJ TQAZS ZMJGD LTCELK ICCQ UAGV YG KIL XG EGLWX KILWKQFW F YDCE TGAIFT A TUKJ KYOIKK UFC LWF SFZ AXF XJL MFC TX KIL NX UNJ YZQ FRXL FBZSY U YMJJ PI YJZQBVMW XU CF DM FR QS XU ETO KIL PFAQ KMW FOEJ QAOCQ TQ MDZJRCEL KAIE","smurf")
=="la la la la la la sing a happy song la la la la la la smurf it all day long la la la la la la smurf along with me la la la la la la simple as can be next time youre feeling blue just let a smile begin happy things will come to you so smurf yourself a grin oooooo i hate smurfs ill get you ill get all of you if its the last thing i ever do hehehehe la la la la la la now you know the tune youll be smurfing soon")
print("\n***VIGENERE BREAK***")
print(VIGENERE.breakVigenere("DM FR QS XU CF DM MZSY M BRUHK MFSY XU CF DM FR QS XU JRMDZ ZY SXF UFQ XIEL DM FR QS XU CF DM MDZJR UCTFS QZYZ YY CF DM FR QS XU CF KUGGQW MM TFF NY EJPF NZRW KILWW RYVQAZA SQMQ DLXL XYK F KYCCJ TQAZS ZMJGD LTCELK ICCQ UAGV YG KIL XG EGLWX KILWKQFW F YDCE TGAIFT A TUKJ KYOIKK UFC LWF SFZ AXF XJL MFC TX KIL NX UNJ YZQ FRXL FBZSY U YMJJ PI YJZQBVMW XU CF DM FR QS XU ETO KIL PFAQ KMW FOEJ QAOCQ TQ MDZJRCEL KAIE")=="smurf")
