today_subject = [ "Biology", "Physics", "General Maths", "Chemistry" ] 
while True : 
    tomorrow_subject = input(f"Agamikal kon subject porbe? lekha shesh hole 'done' likho")  .strip ()     
    if tomorrow_subject == "done" : 
        break 
    else : 
        today_subject .append( tomorrow_subject )                         
today_subject .sort( ) 
print ( " Sorted today subject " ) 
for i in range( len( today_subject ) ) : 
    print ( str ( i + 1 ) + " . " + today_subject [ i ]) 
    print ( " index "   +  str ( i + 1 ) +  today_subject [ i ] )      
search_subject = input ( f" Apni kon subject ti khujte chan ? " ) .strip ( ) 
if search_subject in today_subject : 
        print ( " Ha : " + search_subject + " list a ache " ) 
        pos = today_subject .index( search_subject )
        print ( " index number : " + str ( pos ) )        
else : 
       print ( " sorry ! " + search_subject + " list a paoa ji ni " ) 