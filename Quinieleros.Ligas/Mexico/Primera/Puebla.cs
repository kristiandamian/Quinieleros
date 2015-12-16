using System;

namespace Quinieleros.Ligas
{
	public class Puebla : EquipoMexico
	{
		public Puebla ()
		{
			this.Apodos = new System.Collections.Generic.List<string> (){ "La franja","Los camoteros" };
			this.Nombre = "Puebla";
			this.Icon = "";
			this.id = "PUEBLA";
		}
	}
}

