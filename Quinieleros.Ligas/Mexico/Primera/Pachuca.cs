using System;

namespace Quinieleros.Ligas
{
	public class Pachuca : EquipoMexico
	{
		public Pachuca ()
		{
			this.Apodos = new System.Collections.Generic.List<string> (){ "Los tuzos" };
			this.Nombre = "Pachuca";
			this.Icon = "";
			this.id = "PACHUCA";
		}
	}
}

