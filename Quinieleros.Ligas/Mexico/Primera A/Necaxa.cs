using System;

namespace Quinieleros.Ligas
{
	public class Necaxa : EquipoMexico
	{
		public Necaxa ()
		{
			this.Apodos = new System.Collections.Generic.List<string> (){ "Los rayos", "Los electricistas", "Los Once hermanos" };
			this.Nombre = "Necaxa";
			this.Icon = "";
			this.id = "NECAXA";
		}
	}
}

