using System;
using  System.Collections.Generic;

namespace Quinieleros.Ligas
{
	public class Pumas : EquipoMexico
	{
		public Pumas ()
		{
			this.Apodos = new List<string> (){ "Pumas", "Felinos", "Auriazules" };
			this.Nombre = "Pumas UNAM";
			this.Icon = "";
		}
	}
}

