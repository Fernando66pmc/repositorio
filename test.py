# /usr /bin /python
cgi importação
def checkform ():
      print " Content-type : text /html \\ n"
      form = cgi.FieldStorage ()
      se form.has_key ( " nome" ) e formam [" nome" ] value = " . ! " :
            print "
            "
      se form.has_key ( "sobrenome " ) e forma [ "sobrenome "] value = " . ! " :
           print "
      else :
      print " Erro"
      else :
           print" < ; h1> Erro: Não Sexo entrou "
      se form.has_key ( " email " ) e forma [ " email " ] = valor . " " :
           print " E-mail"
      mais: .
           print " Erro" 