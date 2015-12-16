using System;
using System.Collections.Generic;
using Quinieleros.Ligas;
using Quinieleros.Models;

namespace Quinieleros.BO
{
	public class Liga
	{
		public Liga ()
		{
		}

		public static Models.Calendario getCalendario(){
			throw new NotImplementedException ();	//Traer del server 
		}
		public static Models.Jornada getJornada(int numero){
			throw new NotImplementedException ();  //Traer de la base de datos
		}

		public static void GuardoResultados(Models.Jornada resultadosJornada)
		{
			throw new NotImplementedException ();  //Traer de la base de datos
		}
	}

	internal static class LigaDelProyecto
	{
		internal static Ligas.LigaBase getLiga()
		{
			return  Ligas.FactoryLigaMexico.GeneroLigaMexico ();//COMPILACION CONDICIONAL POR SIMBOLOS PARA DETERMINAR LA LIGA
		}
	}
}

