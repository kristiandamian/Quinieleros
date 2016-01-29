function ColorSemaforoDiferenciasGeneradas()
{
    var MaxElementos=5;    
    var elementos=[];    
    $(".diferenciasGeneradas").each(function(){
        elementos.push(parseFloat($(this).text().replace(/,/g,"")))
    });
    elementos.sort(sortNumber);
    if(elementos.length<=MaxElementos)    
        MaxElementos= Math.ceil(elementos.length*.3);//SOLO EL 30% de los elementos
    
    for (var i=0;i<MaxElementos;i++) {
        
       $(".diferenciasGeneradas").each(function(){            
            if(parseFloat($(this).text().replace(/,/g,""))==elementos[i])
            {
                $(this).attr("style","background-color:red; color:white;");
            }
        }); 
    }
}

function sortNumber(a,b) {
    return b-a;
}

function ColorSemaforo(col){
    var PorcentajeVerde=.20;
    var PorcentajeAmarillo=.35;
    $(".semaforo").each(function(){
        var faltante=0;
        $(".monto").each(function(){
            faltante+=parseFloat($(this).text());
        })      
        
        var saldo=parseFloat($(this).parent().find("td:eq("+col+")").text());        
        if (saldo<=(faltante*PorcentajeVerde))//10%
            $(this).attr("style","background-color:green; color:white;");
        if (saldo>(faltante*PorcentajeVerde) && saldo<=(faltante*PorcentajeAmarillo))
            $(this).attr("style","background-color:yellow;");
        if (saldo>(faltante*PorcentajeAmarillo))
            $(this).attr("style","background-color:red; color:white;");
    });
}
 
