print( " acabas de entrar al mundo de agharta")
print(" eres conocido como el hereo de las nieves ")
print( " listo para completar tu ultima aventura ")

print(" caminas por un bosque se te hace familiar pero es por el monton de aventuras pero se hace de noche y necesitas algo que sacas  ")
opcion1= input(" (LINTERNA/ESPADA DE FUEGO) ").lower()

if opcion1 == "linterna":
    print(" enciendes la linterna y te encuentras a un gran oso mutante ")
    print(" que haces ?")
    opcion1 = input(" CORRER\ESCONDERTE\PELEAR ").lower()
    
    if opcion1== "correr":  
      print(" decides correr sin cansancio hasta ves una cueva donde puedes perder al oso ")
      print(" que decides hacer")
      opcion1= input ( "CRUZAR LA CUEVA/ BUSCAR OTRO CAMINO/RODEAR LA CUEVA ").lower()
      
      if opcion1 == "cruzar la cueva":
        print(" cruzas la cueva y pierdes al oso quedando agotado y sin refugio ")
        print(" que haces ahora ?")
        opcion1=input(" (DESCANSAR/HACER UN REFUGIO/EXPLORAR)").lower()

        if opcion1 == "descansar":
           print(" descansas a las afuera de la cueva despertandote escuchas aullidos")
           print(" cual es tu plan ahora?")
           opcion1=input("(QUEDARSE ESCONDIDO\ARMARSE Y PELEAR)").lower()

           if opcion1== "quedarse escondido":
              print(" te quedas escondido hasta el amanecer los lobos no te encuentran")
              print(" sigues tu camino hacia tu casa buena eleccion")
              
           elif opcion1=="armarse y pelear":
              print( " te armas una opcion muy valiente pero los lobos te superan en cantidad")
              print( " a veces ser valiente no es la mejor idea ' GAME OVER ' ")
              
           else :
              print( " operacion invalida, por tramposo y vivo")
              print( " GAME OVERRRR ")
 
        elif opcion1== "hacer un refugio":
           print( " intentas hacer un refugio pierdes tiempo y energia")
           print(" llegan los lobos te atacan has muerto")
           print( " GAMEEEE OVERR ")
        
        elif opcion1 == "explorar":
           print(" no descansas decides continuar encuentras una aldea conocida")
           print(" te recuperas y vuelves a tu hogar !!! EXITOOOSSS !!! ")
        
        else:
           print(" opcion erronea pierdes tiempo game over")
        
      elif opcion1 =="rodear la cueva":
         print(" rodeas la cueva pero el oso sigue detras de ti")
         print(" necesitas nuevas ideas que haces ?")
         opcion1 = input(" RAPIDO/CAUTELOSO/REGRESARTE").lower()
        
         if opcion1 == "rapido" :
            print(" cruzas rapidamente logras escapar del oso y te encuentras una casa donde te recuperas y vuelves a casa")
            print(" goood endinggg ")
         elif opcion1 == "cauteloso":
            print(" caminas lento el oso no te escucha pero para tu mala suerte hay un derrumbe")
            print( " te caen rocas encima GAMEEE OVERRR")
         elif opcion1 == "regresarte": 
            print( " te regresas el oso te atrapa eres su cena GAMEEE OVERRR")
         else: 
            print ( " movimiento invalido gamee overr")
      elif opcion1== "esconderte":
         print(" te escondes del oso en un arbusto te libras de el facilmente")
         print(" el oso se va pero empiezas a escuchar unas voces , que haces ?")
         opcion1=input("(SEGUIR LAS VOCES\QUEDARSE QUIETO\PEDIR AYUDA)")
          
         if opcion1=="seguir las voces":
            print(" sigues las voces se te hacen familiares son tus amigos te ayudan y regresan juntos")
            print(" el poder de la amistad te ha ayudado ")
         elif opcion1== "quedarse quieto":
            print(" te quedas quieto las voces se pierden no sabes a donde ir")
            print(" has perdido ")
         elif opcion1=="pedir ayuda":
            print(" el oso regresa y te come has perdido")
         else:
            print(" opcion incorrecta no escapas el oso te atrapa perdiste")
    elif opcion1 == "pelear" : 
       print(" intentas pelear con el usando una espada de piedra lo haces retroceder pero llegan unos ladrones a la zona")
       print(" que haces ?")
       opcion1= input("HUIR\HABLAR\BATALLA")
       
       if opcion1 == "huir":
          print(" huyes a toda velocidad los bandidos te suiguen pero llegas a una ciudad cercana y te salvas , good ending")
       elif opcion1 == "hablar":
          print(" hablas con ellos no son malas personas solo estan de paso y se asustaron con tu gritos")
          print(" te ayudan sobreviviste , ganaste")
       elif opcion1 == "batalla":
          print(" peleas con ellos son muchos has perdido game over ")
       else:
          print(" movimiento prohibido game over ")
    else:
       print(" opcion no valida el oso te ataca por dudar has perdido")
elif opcion1 == "espada de fuego":
   print(" espada de fuego adquirida ")
   print("tu espada ilumina el bosque el oso se asusta iluminas todo pero escuchas algo entre los arboles")
   opcion1= input(" (SEGUIR\BUSCAR\GUARDAR ESPADA)").lower()
  
   if opcion1 == "seguir":
      print(" sigues el camino hasta una parte secreta del boque y ves unas velas raras ")
      print( " que haces ?")
      opcion1 = input("(INSPECCIONAR\RODEAR\IGNORAR)").lower()

      if opcion1 == "inspeccionar":
         print(" al acercarte era un ritual para abrir un portal magico se abre el portal en frente de ti , que haces ?")
         opcion1= input("(ENTRAR/TOCAR/HUIR)").lower()

         if opcion1 == "entrar":
            print(" entras  te lleva a un reino nuevo nunca antes visto donde hay nuevas aventuras pero contadas en otra oportunidad")
         elif opcion1 == "tocar":
            print(" al tocar el portal ves una camino para escapar una vision magica")
            print(" escapas gracias a la vision y descansas en tu hogar")
         elif opcion1 == "huir":
            print(" te vas ignorando el portal pero te das cuenta que el bosque es infinito")
            print(" pierdes quedando atrapado por siempre ")
         else:
            print(" opcion erronea pierdes todo y desapareces ")
      elif opcion1 == "rodear":
         print(" rodeas las velas con cuidado cruzas  una colina y te das cuenta")
         print(" ves el camino para llegar a tu casa ganasteeee ")
      elif opcion1 == "ignorar":
         print( " ignoras las velas pero caes en una fatal trampa del mago oscuro del bosque game over ")
      else:
         print(" opcio incorrecta has perdido por leer mal permabaneado")
  
   elif opcion1 == "buscar":
      print(" ves dentro los arboles y ves una mascota magica herida que haces ?")
      opcion1=input("AYUDAR/DEJARLO").lower()

      if opcion1 == "ayuda":
         print(" decides ayudarlo y lo curas con medicinas y kits de primer auxilio que traias en tu bolso")
         print(" te ayuda al curarse se va contigo y llegan a tu casa sanos y salvos , nuevo amigo")
      elif opcion1 == "dejarlo":
         print(" lo dejas y muere pero al morir explota todo el bosque y te mata game overr")
      else:
         print(" jugada incorrecta has sido eliminado")
   elif opcion1 == "guardar espada":
      print(" guardas tu espada y te escondes al rato no escuchas nada ")
      print( " estas en un silencio incomodo cual es tu siguiente paso ?")
      opcion1=input("(SACAR TU ESPADA DE NUEVO\ SEGUIR OCULTO\ REZAR)").lower()

      if opcion1 == "sacar tu espada":
         print( " al sacar tu espada de fuego de nuevo ves a tu alrededor y no ves ni escuchas nada")
         print( " te vas y sigues tu camino hacia tu casa un final aburrido")
      elif opcion1 == "sigues oculto":
         print(" sigues oculto hasta que se abre la tierra y te come")
         print(' pierdes porq el bosque te comio')
      elif opcion1 == "rezar":
         print(" rezas y despiertas en tu cama sano y salvo a sucedido un milagro divino")
      else:
        print(" opcion invalida  pierdes el juego casi al final ")
else:
   print("opcion incorrecta va a explotar tu pc")


print (" gracias por jugar el juego del anio G.O.T.Y. no se lo den a expedition 33 ")
         

            
       

        

      
        
           
           
             
                
            
        
          
