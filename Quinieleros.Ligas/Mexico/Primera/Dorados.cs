using System;
using System.Collections.Generic;

namespace Quinieleros.Ligas
{
	public class Dorados : EquipoMexico
	{
		public Dorados ()
		{
			this.Apodos = new List<string> (){ "El gran pez", "los Dorados" };
			this.Nombre = "Dorados de Sinaloa";
			this.Icon = "";
			this.id = "DORADOS";
		}
	}
}

