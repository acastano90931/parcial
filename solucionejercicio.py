def imprimirRecorrido(arr,n):
    
    inicio = 0
    
    surtidor = 0         
    distancia = 0        

    for i in range(n):
      surtidor += arr[i][0] - arr[i][1]
      if surtidor < 0:          
        inicio = i+1        
        distancia += surtidor            
        surtidor = 0            
     
 
    return inicio if (surtidor+distancia)>=0 else -1
   

arr = [[4,6], [6,5], [7,3], [4,5]]
inicio= imprimirRecorrido(arr,4)
if inicio == -1:
  print("!!!")
else:
  print("Surtido de Inicio = {}".format(inicio))
 
##basado en un ejemplo que encontrĂ© en el mismo gitHub