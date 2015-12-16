using System;

namespace Quinieleros.Ligas
{
	public class Leon : EquipoMexico
	{
		public Leon ()
		{
			this.Apodos = new System.Collections.Generic.List<string> (){ "Los panzas verdes","Los esmeraldas", "León" };
			this.Nombre = "León";
			this.Icon = "";
			this.id = "LEON";
		}
	}
}

